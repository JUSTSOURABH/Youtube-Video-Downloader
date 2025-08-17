"""
YouTube Video Downloader
------------------------
Author: Sourabh Nimoda
Description:
    Simple script to download YouTube videos in the highest resolution.
"""

from pytubefix import YouTube


def main():
    link = input("🔗 Enter the URL of the video: ")
    yt = YouTube(link)

    print(f"\n📌 Title: {yt.title}")
    print("⬇️ Downloading...")
    yt.streams.get_highest_resolution().download(output_path="downloads")
    print("✅ Download completed! Saved in 'downloads' folder.")


if __name__ == "__main__":
    main()
