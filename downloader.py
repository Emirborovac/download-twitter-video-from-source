import subprocess

def download_and_combine_m3u8(video_url, audio_url, output_file):
    try:
        # Use ffmpeg to download and combine video and audio streams
        command = [
            'ffmpeg',
            '-i', video_url,  # Input video URL (without audio)
            '-i', audio_url,  # Input audio URL
            '-c:v', 'copy',   # Copy video codec without re-encoding
            '-c:a', 'copy',   # Copy audio codec without re-encoding
            output_file       # Output file path
        ]
        subprocess.run(command, check=True)
        print(f"Video successfully downloaded and combined: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        print("Failed to download or combine the video and audio.")

if __name__ == "__main__":
    # URL of the video (no audio) .m3u8 file
    video_url = 'https://video.twimg.com/ext_tw_video/1841913233424121856/pu/pl/avc1/1280x720/kjcV7zDLWcrI2jtM.m3u8'  # Replace with actual video URL
    
    # URL of the audio .m3u8 file
    audio_url = 'https://video.twimg.com/ext_tw_video/1841913233424121856/pu/pl/mp4a/128000/dRdOlzyq8fC_S9NE.m3u8'  # Replace with actual audio URL
    
    # Output file name
    output_file = r'C:\Users\Ymir\Downloads\testing_video.mp4'
    
    # Download and combine video and audio streams
    download_and_combine_m3u8(video_url, audio_url, output_file)
