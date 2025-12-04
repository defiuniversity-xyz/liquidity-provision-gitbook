#!/usr/bin/env python3
"""
Fix audio file MIME types in GCS to make them playable in GitBook.
Updates Content-Type from 'audio/mp4a-latm' to 'audio/mp4' for all .m4a files.
"""

from google.cloud import storage
import os
import sys
from pathlib import Path

# Configuration
SCRIPT_DIR = Path(__file__).parent
GITBOOK_DIR = SCRIPT_DIR.parent
ROOT_DIR = GITBOOK_DIR.parent.parent
SERVICE_ACCOUNT_PATH = os.getenv(
    'GOOGLE_APPLICATION_CREDENTIALS',
    str(ROOT_DIR / "Keys" / "google-service-account.json")
)
BUCKET_NAME = os.getenv('GCS_BUCKET_NAME', 'liquidity-provision-media')
PROJECT_ID = 'defi-university'

def fix_audio_mime_types():
    """Update Content-Type metadata for all audio files in GCS"""
    
    # Verify service account file exists
    if not os.path.exists(SERVICE_ACCOUNT_PATH):
        print(f"ERROR: Service account file not found: {SERVICE_ACCOUNT_PATH}")
        print("Please set GOOGLE_APPLICATION_CREDENTIALS environment variable or ensure")
        print("Keys/google-service-account.json exists relative to project root")
        return False
    
    # Set environment variable for Google Cloud authentication
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.abspath(SERVICE_ACCOUNT_PATH)
    
    # Setup Google Cloud Storage client
    try:
        storage_client = storage.Client(project=PROJECT_ID)
        bucket = storage_client.bucket(BUCKET_NAME)
        
        if not bucket.exists():
            print(f"ERROR: Bucket '{BUCKET_NAME}' does not exist")
            return False
        
        print(f"✓ Connected to bucket: {BUCKET_NAME}")
    except Exception as e:
        print(f"ERROR: Failed to connect to Google Cloud Storage: {e}")
        return False
    
    # Find all audio files in lesson-XX/audio/ directories
    print(f"\nSearching for audio files in gs://{BUCKET_NAME}/...")
    print("=" * 60)
    
    blobs_to_fix = []
    
    # List all blobs in the bucket
    for blob in bucket.list_blobs(prefix='lesson-'):
        # Check if it's an audio file in an audio directory
        if '/audio/' in blob.name and blob.name.endswith('.m4a'):
            # Check current content type
            blob.reload()  # Ensure we have latest metadata
            current_type = blob.content_type
            
            if current_type != 'audio/mp4':
                blobs_to_fix.append((blob, current_type))
                print(f"Found: {blob.name}")
                print(f"  Current Content-Type: {current_type}")
    
    if not blobs_to_fix:
        print("\n✓ No audio files need updating (all already have audio/mp4)")
        return True
    
    print(f"\n{'='*60}")
    print(f"Found {len(blobs_to_fix)} audio files to update")
    print(f"{'='*60}\n")
    
    # Update each file
    updated = []
    failed = []
    
    for blob, old_type in blobs_to_fix:
        try:
            print(f"Updating: {blob.name}")
            print(f"  Old: {old_type} → New: audio/mp4")
            
            # Update content type
            blob.content_type = 'audio/mp4'
            blob.patch()
            
            # Verify the update
            blob.reload()
            if blob.content_type == 'audio/mp4':
                print(f"  ✓ Successfully updated")
                updated.append(blob.name)
            else:
                print(f"  ✗ Update failed - still shows: {blob.content_type}")
                failed.append(blob.name)
            
        except Exception as e:
            print(f"  ✗ Error updating {blob.name}: {e}")
            failed.append(blob.name)
    
    # Summary
    print(f"\n{'='*60}")
    print("Update Summary:")
    print(f"{'='*60}")
    print(f"✅ Successfully updated: {len(updated)} files")
    print(f"❌ Failed: {len(failed)} files")
    
    if updated:
        print(f"\nUpdated files:")
        for filename in updated:
            print(f"  ✓ {filename}")
    
    if failed:
        print(f"\nFailed files:")
        for filename in failed:
            print(f"  ✗ {filename}")
    
    print(f"\n{'='*60}")
    print("Next steps:")
    print("1. Verify audio files in GitBook now show as playable players")
    print("2. Test by viewing any lesson page")
    print(f"{'='*60}\n")
    
    return len(failed) == 0

if __name__ == "__main__":
    success = fix_audio_mime_types()
    sys.exit(0 if success else 1)

