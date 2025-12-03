# Liquidity Provision GitBook Media Upload Setup

This guide explains how to upload audio and video files to Google Cloud Storage and integrate them into the GitBook lessons.

## Prerequisites

- Google Cloud account with project: `defi-university`
- Service account JSON file: `Keys/google-service-account.json`
- Python dependencies installed: `pip install -r tools/requirements.txt`

## Step 1: Create GCS Bucket

The bucket `liquidity-provision-media` needs to be created before uploading files.

### Option A: Using Google Cloud Console (Recommended)

1. Log in to [Google Cloud Console](https://console.cloud.google.com)
2. Select project: **defi-university**
3. Navigate to **Cloud Storage** > **Buckets**
4. Click **Create bucket**
5. Configure:
   - **Name**: `liquidity-provision-media` (must be globally unique)
   - **Location type**: Region (e.g., `us-central1`)
   - **Storage class**: Standard
   - **Access control**: Uniform (recommended)
6. Click **Create**

### Option B: Using gcloud CLI

```bash
gcloud storage buckets create gs://liquidity-provision-media \
  --project=defi-university \
  --location=us-central1 \
  --uniform-bucket-level-access
```

## Step 2: Configure Public Access

1. Go to bucket > **Permissions** tab
2. Click **Grant Access**
3. Configure:
   - **New principals**: `allUsers`
   - **Role**: `Storage Object Viewer`
4. Click **Save**
5. Confirm the warning about making bucket publicly accessible

## Step 3: Configure CORS

1. In your bucket, go to **Configuration** tab
2. Scroll to **CORS configuration**
3. Click **Edit CORS configuration**
4. Paste this JSON configuration:

```json
[
  {
    "origin": ["https://docs.gitbook.com", "https://*.gitbook.io", "http://localhost:3000"],
    "method": ["GET", "HEAD"],
    "responseHeader": ["Content-Type", "ETag"],
    "maxAgeSeconds": 3600
  }
]
```

5. Click **Save**

## Step 4: Upload Media Files

Once the bucket is created and configured, upload all media files:

```bash
cd ebooks/liquidity-provision-gitbook/tools
python3 upload_all_media.py
```

This will upload:
- 12 audio files from `content/audio/` (`.m4a` files)
- 12 video files from `content/videos/` (`.mp4` files)

Files will be organized in GCS as:
- `liquidity-provision-media/lesson-01/audio/lesson1 AMM_Explained_The_$x__cdot_y_=_k$_Formula.m4a`
- `liquidity-provision-media/lesson-01/video/lesson1 Automated_Market_Makers.mp4`
- (and similarly for lessons 02-12)

## Step 5: Verify Embeds in Lesson Files

The embed tags have already been added to all lesson files. Each lesson file now has:

```markdown
{% embed url="https://storage.googleapis.com/liquidity-provision-media/lesson-XX/audio/filename.m4a" %}
{% embed url="https://storage.googleapis.com/liquidity-provision-media/lesson-XX/video/filename.mp4" %}

# Lesson Title
...
```

The audio embed appears first (as a playable button), followed by the video embed, then the lesson content.

## Verification

After uploading:

1. **Check GCS Console**: Verify files appear in correct folders
2. **Test URLs**: Open each URL in browser to verify public access
3. **Test Playback**: Verify audio/video files play correctly
4. **Test GitBook**: Verify embeds display correctly in GitBook preview

## Troubleshooting

### Upload Fails with "Bucket does not exist"
- Ensure bucket `liquidity-provision-media` has been created
- Verify bucket name matches in `upload_asset.py` (default: `liquidity-provision-media`)

### Upload Fails with "Permission Denied"
- Check service account has `Storage Object Admin` role on bucket
- Verify service account JSON file path is correct

### Files Download Instead of Playing
- Check MIME type is set correctly (script handles this automatically)
- Verify `content_type` is set in blob metadata
- Ensure bucket has public access configured

### CORS Errors in Browser
- Verify CORS policy includes GitBook domains
- Check `origin` includes your GitBook domain
- Clear browser cache and try again

### Service Account Not Found
- Verify `Keys/google-service-account.json` exists
- Check file path is correct relative to project root
- Set `GOOGLE_APPLICATION_CREDENTIALS` environment variable explicitly

## Scripts Reference

- `upload_asset.py` - Upload individual files to GCS
- `upload_all_media.py` - Batch upload all audio and video files
- `add_media_embeds.py` - Add embed tags to lesson files (already run)
- `create_bucket.py` - Attempt to create bucket programmatically (requires bucket creation permissions)

## File Structure

```
liquidity-provision-gitbook/
├── content/
│   ├── audio/          # 12 .m4a audio files
│   ├── videos/         # 12 .mp4 video files
│   └── lessons/        # 12 lesson markdown files (with embeds)
└── tools/
    ├── upload_asset.py
    ├── upload_all_media.py
    ├── add_media_embeds.py
    └── requirements.txt
```

## Notes

- Audio files use GitBook's `{% embed %}` syntax which creates a playable audio player (not a download link)
- Audio embed appears first, then video embed, then lesson content
- All 12 lessons have been updated with embed tags
- Once files are uploaded to GCS, the embeds will work automatically in GitBook

