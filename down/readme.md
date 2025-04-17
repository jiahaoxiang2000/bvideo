# download the video from the douyin

We found the [f2](https://github.com/Johnserf-Seed/f2) project, which supports video downloading. Initially, we considered using its API to obtain the video URL, but much of the logic is tightly coupled with the CLI functionality. To quickly implement the basic feature, we decided to use the CLI directly to download videos.

## Install f2

You can automate the installation process using a `Makefile`.  
First, ensure you have `uv` installed. Then, run:

```sh
make f2-init
```

This will:

- Create a virtual environment with `uv`
- Activate the environment
- Install dependencies
- Install f2 in editable mode

Alternatively, you can follow the manual steps below:

here we use the install way from the code resource, so first we need use the `uv` to create the virtual environment, then activate it, install the dependencies, and finally install the f2 by the `pip install -e .` on the `f2` folder.

## use CLI to download the video

You can use the Makefile to download videos with the CLI in the activated Python virtual environment:

```sh
make f2-download
```

This will run the CLI command `f2 dy -c down/like.yaml` using the Python environment set up previously.  
The downloaded files will be saved in the `Download/douyin/like/$UserName/` folder.

For reference, see the [CLI configure list](https://f2.wiki/guide/apps/douyin/cli).  
Here we use the user's _like_ video collection as the target.

## the use the lib to combine the video

ffmpeg is a powerful tool that can be used to combine multiple video files into one.

Suppose your downloaded videos are in the `Download/douyin/like/isomo/` folder.  
To combine all videos in that folder, you can use the Makefile:

```sh
make combine-videos
```

This will run a Python script (`combine_videos.py`) that automatically finds all `.mp4` files in the folder and uses ffmpeg to merge them into `output.mp4` (no intermediate file list needed).

**Troubleshooting:**

- If you see errors about missing files or directories, ensure your videos are downloaded to `Download/douyin/like/isomo/`.
- All videos should have the same codec and resolution for best results.

**Note:**

- Ensure all videos have the same codec and resolution for best results.
- The files will be combined in the order returned by the glob pattern (usually alphabetical).

## upload the combined video to Bilibili

To upload `output.mp4` to Bilibili, you can use the [bilibili-api](https://github.com/Nemo2011/bilibili-api) Python library or upload manually via the Bilibili website.

### Using Python (bilibili-api)

1. Install the library:
   ```sh
   uv pip install bilibili-api-python
   ```
2. Refer to the [bilibili-api-python documentation](https://github.com/Nemo2011/bilibili-api) for authentication and upload usage.

### Manual Upload

1. Go to [Bilibili upload page](https://member.bilibili.com/platform/upload/video/).
2. Select `output.mp4` and fill in the required information.
3. Submit your video.
