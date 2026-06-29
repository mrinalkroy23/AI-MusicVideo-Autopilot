from typing import List

class LyricsSegmenter:
    def segment(self, lyrics:str, lines_per_scene:int=4) -> List[str]:
        lines=[l.strip() for l in lyrics.splitlines() if l.strip()]
        scenes=[]
        for i in range(0,len(lines),lines_per_scene):
            scenes.append('\n'.join(lines[i:i+lines_per_scene]))
        return scenes

class ScenePlanner:
    def create_plan(self, scenes:List[str]) -> List[dict]:
        output=[]
        for idx,scene in enumerate(scenes, start=1):
            output.append({
                'scene_id': idx,
                'duration_seconds': 8,
                'lyrics': scene
            })
        return output
