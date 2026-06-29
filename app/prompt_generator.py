class PromptGenerator:
    STYLE = 'Ultra realistic cinematic music video, 4K, dramatic lighting, consistent hero and vehicle.'

    def generate(self, scene_plan:list):
        prompts=[]
        for item in scene_plan:
            prompts.append({
                'scene_id': item['scene_id'],
                'prompt': f"{self.STYLE} Scene based on lyrics: {item['lyrics']}"
            })
        return prompts
