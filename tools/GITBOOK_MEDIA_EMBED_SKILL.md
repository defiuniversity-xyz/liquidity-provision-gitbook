# GitBook Media Embed Integration Skill

This document captures the complete process for integrating audio and video files into GitBook courses with proper formatting, CORS configuration, and URL encoding.

## Overview

When integrating audio and video files from Google Cloud Storage into GitBook, three critical components must be configured correctly:

1. **CORS Configuration** - Allows GitBook to access files from GCS
2. **URL Encoding** - Ensures special characters in filenames work in browsers
3. **Formatting** - Matches investor mindset format for consistency

## Step 1: Upload Media Files to Google Cloud Storage

### Prerequisites
- Google Cloud Storage bucket created
- Service account with Storage Object Admin permissions
- Media files ready (audio .m4a and video .mp4)

### Upload Process
```bash
cd ebooks/[course-name]-gitbook/tools
python3 upload_all_media.py
```

Files are organized in GCS as:
- `[bucket-name]/lesson-XX/audio/filename.m4a`
- `[bucket-name]/lesson-XX/video/filename.mp4`

## Step 2: Configure CORS for GitBook Access

**Critical:** Without CORS configuration, GitBook cannot load media files from GCS.

### Create CORS Configuration File
Create `tools/cors-config.json`:
```json
[{
  "origin": ["https://docs.gitbook.com", "https://*.gitbook.io", "http://localhost:3000"],
  "method": ["GET", "HEAD"],
  "responseHeader": ["Content-Type", "ETag"],
  "maxAgeSeconds": 3600
}]
```

### Apply CORS Configuration
```bash
gsutil cors set cors-config.json gs://[bucket-name]
```

### Verify CORS Configuration
```bash
gsutil cors get gs://[bucket-name]
```

Expected output:
```json
[{"maxAgeSeconds": 3600, "method": ["GET", "HEAD"], "origin": ["https://docs.gitbook.com", "https://*.gitbook.io", "http://localhost:3000"], "responseHeader": ["Content-Type", "ETag"]}]
```

## Step 3: Configure Public Access

Ensure bucket allows public read access:

```bash
gsutil iam ch allUsers:objectViewer gs://[bucket-name]
```

## Step 4: Add Embed Tags to Lesson Files

### Format Pattern (Investor Mindset Style)

The correct format for embed tags in lesson files:

```markdown
{% embed url="[URL-ENCODED-AUDIO-URL]" %}

{% embed url="[URL-ENCODED-VIDEO-URL]" %}

# Lesson Title
```

**Key Points:**
- Audio embed on line 1
- **Blank line** (line 2)
- Video embed on line 3
- **Blank line** (line 4)
- Lesson content starts on line 5

### URL Encoding Requirements

**Critical:** Filenames with special characters MUST be URL-encoded:
- Spaces → `%20`
- Dollar signs (`$`) → `%24`
- Equals signs (`=`) → `%3D`
- Underscores (`_`) → remain as-is (safe character)

**Example:**
```
Original: lesson1 AMM_Explained_The_$x__cdot_y_=_k$_Formula.m4a
Encoded:  lesson1%20AMM_Explained_The_%24x__cdot_y_%3D_k%24_Formula.m4a
```

### Using the Embed Script

The `add_media_embeds.py` script automatically:
- Finds audio and video files for each lesson
- Generates properly URL-encoded GCS URLs
- Adds embeds in the correct format with blank lines

```bash
python3 tools/add_media_embeds.py
```

## Step 5: Fix URL Encoding (If Needed)

If lesson files already have embeds but URLs aren't encoded:

```bash
python3 tools/fix_url_encoding.py
```

This script:
- Finds all embed tags with GCS URLs
- URL-encodes the filename portion
- Preserves the rest of the URL structure

## Step 6: Fix Embed Formatting (If Needed)

If embeds exist but formatting is incorrect (missing blank lines):

```bash
python3 tools/fix_embed_formatting.py
```

This ensures:
- Blank line between audio and video embeds
- Blank line after video embed before content

## Verification Checklist

Before pushing to GitHub, verify:

- [ ] CORS is configured: `gsutil cors get gs://[bucket-name]`
- [ ] Public access enabled: `gsutil iam get gs://[bucket-name]` shows `allUsers:objectViewer`
- [ ] URLs are URL-encoded (check for `%20`, `%24`, `%3D` in embed tags)
- [ ] Formatting has blank lines between embeds
- [ ] All 12 lessons have both audio and video embeds
- [ ] Test URL accessibility: `curl -I "[encoded-url]"` returns HTTP 200

## Common Issues and Solutions

### Issue: Media files don't show in GitBook

**Symptoms:** Embed tags are present but no player appears

**Causes:**
1. CORS not configured → Check: `gsutil cors get gs://[bucket-name]`
2. URLs not encoded → Check embed tags for special characters
3. Bucket not public → Check: `gsutil iam get gs://[bucket-name]`

**Solution:**
```bash
# 1. Configure CORS
gsutil cors set cors-config.json gs://[bucket-name]

# 2. Fix URL encoding
python3 tools/fix_url_encoding.py

# 3. Verify public access
gsutil iam ch allUsers:objectViewer gs://[bucket-name]
```

### Issue: 404 errors when accessing files

**Cause:** Filename in URL doesn't match actual filename in GCS

**Solution:**
- Verify actual filename in GCS: `gsutil ls gs://[bucket-name]/lesson-01/audio/`
- Ensure URL encoding matches actual filename
- Check for typos in embed URLs

### Issue: CORS errors in browser console

**Cause:** CORS configuration missing or incorrect

**Solution:**
```bash
# Re-apply CORS configuration
gsutil cors set cors-config.json gs://[bucket-name]

# Verify it's applied
gsutil cors get gs://[bucket-name]
```

## Script Reference

### `upload_all_media.py`
- Uploads all audio and video files to GCS
- Organizes by lesson number
- Sets correct MIME types

### `add_media_embeds.py`
- Adds embed tags to lesson files
- Generates URL-encoded URLs
- Creates correct formatting with blank lines

### `fix_url_encoding.py`
- Fixes existing embed tags with unencoded URLs
- Preserves formatting
- Only updates URLs that need encoding

### `fix_embed_formatting.py`
- Adds blank lines between embeds
- Ensures consistent formatting
- Idempotent (safe to run multiple times)

## File Structure

```
[course-name]-gitbook/
├── content/
│   └── lessons/
│       ├── lesson-01-*.md  (with embeds at top)
│       ├── lesson-02-*.md
│       └── ...
├── tools/
│   ├── upload_all_media.py
│   ├── add_media_embeds.py
│   ├── fix_url_encoding.py
│   ├── fix_embed_formatting.py
│   └── cors-config.json
└── .gitbook.yaml
```

## Example: Complete Integration Workflow

```bash
# 1. Upload media files
cd ebooks/[course]-gitbook/tools
python3 upload_all_media.py

# 2. Configure CORS
gsutil cors set cors-config.json gs://[bucket-name]

# 3. Ensure public access
gsutil iam ch allUsers:objectViewer gs://[bucket-name]

# 4. Add embeds to lessons
python3 add_media_embeds.py

# 5. Verify formatting
head -5 ../content/lessons/lesson-01-*.md

# 6. Commit and push
git add content/lessons/*.md tools/
git commit -m "Add audio/video embeds with proper formatting and encoding"
git push origin main
```

## Testing

### Test CORS Configuration
```bash
curl -H "Origin: https://docs.gitbook.com" \
     -H "Access-Control-Request-Method: GET" \
     -X OPTIONS \
     "[encoded-url]" \
     -v | grep -i "access-control"
```

Should return:
```
< access-control-allow-origin: https://docs.gitbook.com
< access-control-max-age: 3600
< access-control-allow-methods: GET,HEAD
```

### Test URL Accessibility
```bash
curl -I "[encoded-url]"
```

Should return:
```
HTTP/2 200
content-type: audio/mp4a-latm  (or video/mp4)
```

## Key Takeaways

1. **CORS is mandatory** - GitBook cannot access GCS files without it
2. **URL encoding is critical** - Special characters break embed functionality
3. **Formatting matters** - Blank lines ensure proper rendering
4. **Always verify** - Test URLs and CORS before pushing to production

## Related Files

- `MEDIA_UPLOAD_SETUP.md` - Complete media upload guide
- `GCS_SETUP_GUIDE.md` - GCS bucket setup (if needed)
- `add_media_embeds.py` - Embed generation script
- `fix_url_encoding.py` - URL encoding fix script
- `fix_embed_formatting.py` - Formatting fix script

