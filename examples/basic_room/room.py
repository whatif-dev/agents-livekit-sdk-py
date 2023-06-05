import livekit
import asyncio

URL = 'ws://localhost:7880'
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5MDY2MTMyODgsImlzcyI6IkFQSVRzRWZpZFpqclFvWSIsIm5hbWUiOiJuYXRpdmUiLCJuYmYiOjE2NzI2MTMyODgsInN1YiI6Im5hdGl2ZSIsInZpZGVvIjp7InJvb20iOiJ0ZXN0Iiwicm9vbUFkbWluIjp0cnVlLCJyb29tQ3JlYXRlIjp0cnVlLCJyb29tSm9pbiI6dHJ1ZSwicm9vbUxpc3QiOnRydWV9fQ.uSNIangMRu8jZD5mnRYoCHjcsQWCrJXgHCs0aNIgBFY'


async def main():
    room = livekit.Room()
    await room.connect(URL, TOKEN)

    @room.on("participant_connected")
    def on_participant_connected(participant: livekit.RemoteParticipant):
        print("participant connected: " + participant.identity)

    @room.on("track_subscribed")
    def on_track_subscribed(track: livekit.Track, publication: livekit.RemoteTrackPublication, participant: livekit.RemoteParticipant):
        if track.kind == livekit.TrackKind.KIND_VIDEO:
            video_stream = livekit.VideoStream(track)

            @video_stream.on("frame_received")
            def on_video_frame(frame: livekit.VideoFrame, buffer: livekit.VideoFrameBuffer):
                argb = livekit.ArgbFrame(
                    livekit.VideoFormatType.FORMAT_ABGR, buffer.width, buffer.height)
                buffer.to_argb(argb)

    print("Connected to room with sid: " + room.sid)
    await room.run()

if __name__ == "__main__":
    asyncio.run(main())
