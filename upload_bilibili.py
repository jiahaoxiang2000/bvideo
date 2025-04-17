import asyncio
from bilibili_api import Credential, video, sync

# Fill in your own SESSDATA, bili_jct, and buvid3 from your browser cookies after logging in to Bilibili
SESSDATA = "your_sessdata"
BILI_JCT = "your_bili_jct"
BUVID3 = "your_buvid3"

VIDEO_PATH = "Download/douyin/like/isomo/output.mp4"
TITLE = "My Douyin Video Collection"
DESC = "Combined Douyin liked videos, uploaded automatically."
TAGS = ["douyin", "bilibili", "video", "auto-upload"]

async def main():
    cred = Credential(SESSDATA, BILI_JCT, BUVID3)
    v = video.VideoUploader(cred)
    # Upload video
    print("Uploading video...")
    result = await v.upload(
        video_path=VIDEO_PATH,
        title=TITLE,
        desc=DESC,
        tags=TAGS,
        copyright=2,  # 2 = original, 1 = reprint
        source="https://www.douyin.com/",
        cover=None,  # You can specify a cover image path if needed
        dynamic=DESC
    )
    print("Upload finished.")
    print("Video publish status:", result)

if __name__ == "__main__":
    sync(main())
