import os
from subprocess import getoutput

os.system(f"pip install --upgrade pip")

gpu_info = getoutput('nvidia-smi')
if("A10G" in gpu_info):
    os.system(f"pip install -q https://github.com/camenduru/stable-diffusion-webui-colab/releases/download/0.0.15/xformers-0.0.15.dev0+4c06c79.d20221205-cp38-cp38-linux_x86_64.whl")
elif("T4" in gpu_info):
    os.system(f"pip install -q https://github.com/camenduru/stable-diffusion-webui-colab/releases/download/0.0.15/xformers-0.0.15.dev0+1515f77.d20221130-cp38-cp38-linux_x86_64.whl")

os.system(f"git clone https://github.com/OswaldDevolpment/stable-diffusion-webui /home/user/app/stable-diffusion-webui")
os.chdir("/home/user/app/stable-diffusion-webui")

# ----------------------------Please duplicate this space and delete this block if you don't want to see the extra header----------------------------
os.system(f"wget -q https://github.com/OswaldDevolpment/webuij/raw/main/header_patch.py -O /home/user/app/header_patch.py")
os.system(f"sed -i -e '/demo:/r /home/user/app/header_patch.py' /home/user/app/stable-diffusion-webui/modules/ui.py")
# ---------------------------------------------------------------------------------------------------------------------------------------------------

os.system(f"wget -q https://github.com/OswaldDevolpment/webuij/raw/main/env_patch.py -O /home/user/app/env_patch.py")
os.system(f"sed -i -e '/import image_from_url_text/r /home/user/app/env_patch.py' /home/user/app/stable-diffusion-webui/modules/ui.py")

# ------------------------------------------------------------------v1.5-----------------------------------------------------------------------------
os.system(f'''sed -i -e "s/document.getElementsByTagName('gradio-app')\[0\].shadowRoot/!!document.getElementsByTagName('gradio-app')[0].shadowRoot ? document.getElementsByTagName('gradio-app')[0].shadowRoot : document/g" /home/user/app/stable-diffusion-webui/script.js''')
os.system(f"sed -i -e 's/                show_progress=False,/                show_progress=True,/g' /home/user/app/stable-diffusion-webui/modules/ui.py")
os.system(f"sed -i -e 's/shared.demo.launch/shared.demo.queue().launch/g' /home/user/app/stable-diffusion-webui/webui.py")
os.system(f"sed -i -e 's/ outputs=\[/queue=False, &/g' /home/user/app/stable-diffusion-webui/modules/ui.py")
os.system(f"sed -i -e 's/               queue=False,  /                /g' /home/user/app/stable-diffusion-webui/modules/ui.py")
# ---------------------------------------------------------------------------------------------------------------------------------------------------

if "IS_SHARED_UI" in os.environ:
    os.system(f"sed -i -e '/(modelmerger_interface, \"Checkpoint Merger\", \"modelmerger\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/(train_interface, \"Train\", \"ti\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/extensions_interface, \"Extensions\", \"extensions\"/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/settings_interface, \"Settings\", \"settings\"/d' /home/user/app/stable-diffusion-webui/modules/ui.py")

    os.system(f"rm -rfv /home/user/app/stable-diffusion-webui/scripts/")
    
    os.system(f"wget -q https://github.com/OswaldDevolpment/webuij/raw/main/shared-config.json -O /home/user/app/shared-config.json")
    os.system(f"wget -q https://github.com/OswaldDevolpment/webuij/raw/main/shared-ui-config.json -O /home/user/app/shared-ui-config.json")

    os.system(f"wget -q {os.getenv('MODEL_LINK')} -O /home/user/app/stable-diffusion-webui/models/lora/{os.getenv('MODEL_NAME')}")
    os.system(f"wget -q {os.getenv('VAE_LINK')} -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/{os.getenv('VAE_NAME')}")
    os.system(f"wget -q {os.getenv('YAML_LINK')} -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/{os.getenv('YAML_NAME')}")
    
    os.system(f"python launch.py --force-enable-xformers --disable-console-progressbars --enable-console-prompts --ui-config-file /home/user/app/shared-ui-config.json --ui-settings-file /home/user/app/shared-config.json --no-progressbar-hiding --cors-allow-origins huggingface.co,hf.space")
elif "IS_API" in os.environ:
    os.system(f"sed -i -e '/(txt2img_interface, \"txt2img\", \"txt2img\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/(img2img_interface, \"img2img\", \"img2img\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/(extras_interface, \"Extras\", \"extras\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/(pnginfo_interface, \"PNG Info\", \"pnginfo\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/(modelmerger_interface, \"Checkpoint Merger\", \"modelmerger\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/(train_interface, \"Train\", \"ti\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/extensions_interface, \"Extensions\", \"extensions\"/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/settings_interface, \"Settings\", \"settings\"/d' /home/user/app/stable-diffusion-webui/modules/ui.py")

    os.system(f"wget -q {os.getenv('MODEL_LINK')} -O /home/user/app/stable-diffusion-webui/models/lora/{os.getenv('MODEL_NAME')}")
    os.system(f"wget -q {os.getenv('VAE_LINK')} -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/{os.getenv('VAE_NAME')}")
    os.system(f"wget -q {os.getenv('YAML_LINK')} -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/{os.getenv('YAML_NAME')}")
    
    os.system(f"python launch.py --force-enable-xformers --disable-console-progressbars --enable-console-prompts --ui-config-file /home/user/app/ui-config.json --ui-settings-file /home/user/app/config.json --no-progressbar-hiding --cors-allow-origins=https://camenduru-unity.hf.space --api")
else:
    os.system(f"sed -i -e '/(train_interface, \"Train\", \"ti\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/extensions_interface, \"Extensions\", \"extensions\"/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/settings_interface, \"Settings\", \"settings\"/d' /home/user/app/stable-diffusion-webui/modules/ui.py")

    # Please duplicate this space and delete # character in front of the custom script you want to use or add here more custom scripts with same structure os.system(f"wget -q https://CUSTOM_SCRIPT_URL -O /home/user/app/stable-diffusion-webui/scripts/CUSTOM_SCRIPT_NAME.py")
    os.system(f"wget -q https://gist.github.com/camenduru/9ec5f8141db9902e375967e93250860f/raw/d0bcf01786f20107c329c03f8968584ee67be12a/run_n_times.py -O /home/user/app/stable-diffusion-webui/scripts/run_n_times.py")
    
    # Please duplicate this space and delete # character in front of the extension you want to use or add here more extensions with same structure os.system(f"git clone https://EXTENSION_GIT_URL /home/user/app/stable-diffusion-webui/extensions/EXTENSION_NAME")
    #os.system(f"git clone https://github.com/camenduru/stable-diffusion-webui-artists-to-study /home/user/app/stable-diffusion-webui/extensions/stable-diffusion-webui-artists-to-study")
    os.system(f"git clone https://github.com/yfszzx/stable-diffusion-webui-images-browser /home/user/app/stable-diffusion-webui/extensions/stable-diffusion-webui-images-browser")
    os.system(f"git clone https://github.com/deforum-art/deforum-for-automatic1111-webui /home/user/app/stable-diffusion-webui/extensions/deforum-for-automatic1111-webui")
    os.system(f"git clone https://github.com/toriato/easy-stable-diffusion /home/user/app/stable-diffusion-webui/extensions/easy-stable-diffusion")   
    os.system(f"git clone https://github.com/camenduru/stable-diffusion-webui-converter /home/user/app/stable-diffusion-webui/extensions/stable-diffusion-webui-converter")
    os.system(f"git clone https://github.com/camenduru/batchlinks-webui /home/user/app/stable-diffusion-webui/extensions/batchlinks-webui")
    os.system(f"git clone https://github.com/Akegarasu/sd-webui-model-converter /home/user/app/stable-diffusion-webui/extensions/sd-webui-model-converter")
    os.system(f"git clone https://github.com/arenatemp/stable-diffusion-webui-model-toolkit /home/user/app/stable-diffusion-webui/extensions/stable-diffusion-webui-model-toolkit")
    os.system(f"git clone https://github.com/camenduru/stable-diffusion-webui-huggingface /home/user/app/stable-diffusion-webui/extensions/stable-diffusion-webui-huggingface")
    os.system(f"git clone https://github.com/kohya-ss/sd-webui-additional-networks /home/user/app/stable-diffusion-webui/extensions/sd-webui-additional-networks")
    
    # Please duplicate this space and delete # character in front of the model you want to use or add here more ckpts with same structure os.system(f"wget -q https://CKPT_URL -O /home/user/app/stable-diffusion-webui/models/lora/CKPT_NAME.ckpt")
    os.system(f"wget -q https://huggingface.co/AdamOswald1/sonic/resolve/main/sonicdiffusion_v3Beta3.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/sonicdiffusion_v3Beta3.ckpt")
    os.system(f"wget -q https://huggingface.co/AdamOswald1/test/resolve/main/sonicdiffusion_v3Beta3.safetensors -O /home/user/app/stable-diffusion-webui/models/lora/sonicdiffusion_v3Beta3.safetensors")
    os.system(f"wget -q https://huggingface.co/AdamOswald1/test/resolve/main/sonicdiffusion_v3Beta3.safetensors -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/sonicdiffusion_v3Beta3.safetensors")
    os.system(f"wget -q https://civitai.com/api/download/models/59168?type=Model&format=SafeTensor&size=pruned&fp=fp16 -O /home/user/app/stable-diffusion-webui/models/lora/sonicdiffusion_v3Beta3.safetensors")
    os.system(f"wget -q https://civitai.com/api/download/models/59168?type=Model&format=SafeTensor&size=pruned&fp=fp16 -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/sonicdiffusion_v3Beta3.safetensors")
    #os.system(f"wget -q https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/resolve/main/sd-v1-4.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/sd-v1-4.ckpt")
    #os.system(f"wget -q https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/v1-5-pruned-emaonly.ckpt")
    #os.system(f"wget -q https://huggingface.co/runwayml/stable-diffusion-inpainting/resolve/main/sd-v1-5-inpainting.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/sd-v1-5-inpainting.ckpt")
    #os.system(f"wget -q https://huggingface.co/stabilityai/stable-diffusion-2/resolve/main/768-v-ema.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/768-v-ema.ckpt")
    os.system(f"wget -q https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-inference-v.yaml -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/768-v-ema.yaml")
    os.system(f"wget -q https://huggingface.co/stabilityai/stable-diffusion-2-1/resolve/main/v2-1_768-ema-pruned.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/v2-1_768-ema-pruned.ckpt")
    os.system(f"wget -q https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-inference-v.yaml -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/v2-1_768-ema-pruned.yaml")

    os.system(f"wget -q {os.getenv('MODEL_LINK')} -O /home/user/app/stable-diffusion-webui/models/lora/{os.getenv('MODEL_NAME')}")
    os.system(f"wget -q {os.getenv('VAE_LINK')} -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/{os.getenv('VAE_NAME')}")
    os.system(f"wget -q {os.getenv('YAML_LINK')} -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/{os.getenv('YAML_NAME')}")

    os.system(f"python launch.py --force-enable-xformers --ui-config-file /home/user/app/ui-config.json --ui-settings-file /home/user/app/config.json --disable-console-progressbars --enable-console-prompts --no-progressbar-hiding --cors-allow-origins huggingface.co,hf.space --api --skip-torch-cuda-test")
    
