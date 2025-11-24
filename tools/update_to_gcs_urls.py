#!/usr/bin/env python3
"""
Update markdown files to use Google Cloud Storage URLs instead of local paths.
"""

import re
from pathlib import Path
from typing import List, Tuple


class GCSURLUpdater:
    """Updates image references to use GCS URLs"""
    
    def __init__(self, base_dir: Path, bucket_name: str = "liquidity-provision-gitbook-images"):
        self.base_dir = base_dir
        self.bucket_name = bucket_name
        self.gcs_base_url = f"https://storage.googleapis.com/{bucket_name}"
        self.content_dir = base_dir / "content"
        self.lessons_dir = self.content_dir / "lessons"
        self.exercises_dir = self.content_dir / "exercises"
    
    def local_to_gcs_path(self, local_path: str) -> str:
        """Convert local image path to GCS URL"""
        # Remove leading "images/" if present
        if local_path.startswith("images/"):
            path = local_path[7:]  # Remove "images/" prefix
        else:
            path = local_path
        
        # Construct GCS URL
        gcs_url = f"{self.gcs_base_url}/{path}"
        return gcs_url
    
    def update_file(self, file_path: Path) -> Tuple[int, List[str]]:
        """Update image references in a markdown file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match image markdown: ![alt](path)
        pattern = r'!\[([^\]]+)\]\((images/[^\)]+)\)'
        
        replacements = []
        updated_content = re.sub(
            pattern,
            lambda m: self._replace_image(m, replacements),
            content
        )
        
        if replacements:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
        
        return len(replacements), replacements
    
    def _replace_image(self, match, replacements: List[str]) -> str:
        """Replace a single image reference"""
        alt_text = match.group(1)
        local_path = match.group(2)
        gcs_url = self.local_to_gcs_path(local_path)
        
        replacements.append(f"{local_path} -> {gcs_url}")
        return f"![{alt_text}]({gcs_url})"
    
    def update_all(self) -> dict:
        """Update all markdown files"""
        results = {
            'lessons': {},
            'exercises': {},
            'total_replacements': 0
        }
        
        # Update lesson files
        for lesson_file in sorted(self.lessons_dir.glob("lesson-*.md")):
            count, replacements = self.update_file(lesson_file)
            if count > 0:
                results['lessons'][lesson_file.name] = {
                    'count': count,
                    'replacements': replacements
                }
                results['total_replacements'] += count
        
        # Update exercise files
        for exercise_file in sorted(self.exercises_dir.glob("exercise-*.md")):
            count, replacements = self.update_file(exercise_file)
            if count > 0:
                results['exercises'][exercise_file.name] = {
                    'count': count,
                    'replacements': replacements
                }
                results['total_replacements'] += count
        
        return results


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Update markdown files to use GCS URLs')
    parser.add_argument('--bucket', default='liquidity-provision-gitbook-images',
                       help='GCS bucket name')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be changed without making changes')
    
    args = parser.parse_args()
    
    base_dir = Path(__file__).parent.parent
    updater = GCSURLUpdater(base_dir, bucket_name=args.bucket)
    
    if args.dry_run:
        print("DRY RUN: Would update the following files:")
        # Just show what would be changed
        for lesson_file in sorted(updater.lessons_dir.glob("lesson-*.md")):
            with open(lesson_file, 'r') as f:
                content = f.read()
            matches = re.findall(r'!\[([^\]]+)\]\((images/[^\)]+)\)', content)
            if matches:
                print(f"\n{lesson_file.name}: {len(matches)} images")
                for alt, path in matches[:3]:
                    gcs_url = updater.local_to_gcs_path(path)
                    print(f"  {path} -> {gcs_url}")
                if len(matches) > 3:
                    print(f"  ... and {len(matches) - 3} more")
    else:
        results = updater.update_all()
        print(f"\nUpdate complete!")
        print(f"Total files updated: {len(results['lessons']) + len(results['exercises'])}")
        print(f"Total image references updated: {results['total_replacements']}")
        print(f"\nLessons: {len(results['lessons'])} files")
        print(f"Exercises: {len(results['exercises'])} files")

