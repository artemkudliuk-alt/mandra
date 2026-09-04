import subprocess
import os
import sys
import time

CLI_PATH = r"C:\Users\Jaku\.gemini\config\skills\gpt-image\scripts\generate.py"
OUT_DIR = r"c:\nextweb\mandra\site\assets\founders"

tasks = [
    {
        "name": "pine_bg",
        "out": os.path.join(OUT_DIR, "pine_card_bg_ultra.png"),
        "ref": None,
        "prompt": "Cinematic macro architectural photography of lush evergreen spruce and pine branches with fresh deep green needles, soft natural warm golden bokeh sunlight in background, deep forest dark green tones, atmospheric luxury nature resort aesthetic, zero text, no letters, no watermark, 8k, photorealistic, Hasselblad 50mm f/1.8",
        "size": "landscape"
    },
    {
        "name": "gallery_1",
        "out": os.path.join(OUT_DIR, "gallery_1_hq.png"),
        "ref": os.path.join(OUT_DIR, "gallery_1.jpg"),
        "prompt": "Ultra-luxury glamping dome interior suite, king size bed with crisp neutral linens, cozy drapes, warm wooden flooring, huge floor-to-ceiling panoramic glass window framing peaceful estuary water view, soft morning sunlight, architectural resort interior photography, 8k, photorealistic",
        "size": "landscape"
    },
    {
        "name": "gallery_2",
        "out": os.path.join(OUT_DIR, "gallery_2_hq.png"),
        "ref": os.path.join(OUT_DIR, "gallery_2.jpg"),
        "prompt": "Luxury nature resort outdoor swimming pool with crystal clear turquoise water, stylish sun loungers on timber deck, modern white geodesic dome pavilion in the background, bright clear blue summer sky, boutique eco-resort photography, 8k, photorealistic",
        "size": "landscape"
    },
    {
        "name": "gallery_3",
        "out": os.path.join(OUT_DIR, "gallery_3_hq.png"),
        "ref": os.path.join(OUT_DIR, "gallery_3.jpg"),
        "prompt": "Modern luxury wooden chalets and eco-cottages clustered on a forested hillside among tall evergreen pine trees, illuminated timber staircases and walkways, warm glowing ambient lights, architectural photography, 8k, photorealistic",
        "size": "landscape"
    },
    {
        "name": "gallery_4",
        "out": os.path.join(OUT_DIR, "gallery_4_hq.png"),
        "ref": os.path.join(OUT_DIR, "gallery_4.jpg"),
        "prompt": "Cozy luxury safari glamping tent with extended covered wooden terrace deck, glowing warm festoon string lights, comfortable outdoor beanbag lounge chairs, nestled in birch and pine forest, evening golden hour ambiance, 8k, photorealistic",
        "size": "landscape"
    },
    {
        "name": "gallery_5",
        "out": os.path.join(OUT_DIR, "gallery_5_hq.png"),
        "ref": os.path.join(OUT_DIR, "gallery_5.jpg"),
        "prompt": "Modern black architectural A-frame chalet with steep gable roof, spacious wooden deck terrace, outdoor steaming hot tub bath and loungers, surrounded by towering pine trees in mountain forest, cinematic resort photography, 8k, photorealistic",
        "size": "landscape"
    },
    {
        "name": "gallery_6",
        "out": os.path.join(OUT_DIR, "gallery_6_hq.png"),
        "ref": os.path.join(OUT_DIR, "gallery_6.jpg"),
        "prompt": "Premium safari glamping tents with canvas canopy roofs set on manicured green lawn, surrounded by lush mature trees, serene luxury glamping retreat, bright daytime sunlight, 8k, photorealistic",
        "size": "landscape"
    }
]

def run_task(t):
    print(f"--- Starting {t['name']} ---", flush=True)
    cmd = [
        "python", CLI_PATH,
        "-p", t["prompt"],
        "-f", t["out"],
        "--size", t["size"],
        "--quality", "medium"
    ]
    if t["ref"] and os.path.exists(t["ref"]):
        cmd.extend(["-i", t["ref"]])
    
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    
    res = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"SUCCESS {t['name']}: {t['out']}", flush=True)
    else:
        print(f"ERROR {t['name']}:\nSTDOUT: {res.stdout}\nSTDERR: {res.stderr}", flush=True)

if __name__ == "__main__":
    for t in tasks:
        run_task(t)
        time.sleep(2)
    print("ALL GENERATIONS COMPLETE!", flush=True)
