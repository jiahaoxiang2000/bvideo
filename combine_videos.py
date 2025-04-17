from pathlib import Path
from moviepy import VideoFileClip, concatenate_videoclips

VIDEO_DIR = Path("Download/douyin/like/isomo")
OUTPUT_FILE = VIDEO_DIR / "output.mp4"

def main():
    if not VIDEO_DIR.exists():
        print(f"Directory {VIDEO_DIR} does not exist.")
        print("You need to install the required dependencies first:")
        print("  uv pip install moviepy")
        return
    mp4_files = sorted(VIDEO_DIR.glob("*.mp4"))
    if not mp4_files:
        print(f"No mp4 files found in {VIDEO_DIR}")
        return
    clips = []
    for f in mp4_files:
        try:
            clips.append(VideoFileClip(str(f)))
        except Exception as e:
            print(f"Error loading {f}: {e}")
    if not clips:
        print("No valid video clips to combine.")
        return
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(str(OUTPUT_FILE))
    for clip in clips:
        clip.close()
    print(f"Combined video saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
