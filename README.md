# LLMasOS

pip install letta-client
pip install openai
pip install -U letta
pip install datamodel_code_generator
pip install mcp


docker run \
  -v ~/.letta/.persist/pgdata:/var/lib/postgresql/data \
  -p 8283:8283 \
  -e OPENAI_API_KEY="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" \
  letta/letta:latest

Install ollama first:
sudo apt update && sudo apt upgrade -y
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
curl -fsSL https://ollama.com/install.sh | sh

systemctl edit ollama.service
  [Service]
  Environment="OLLAMA_HOST=0.0.0.0"
systemctl restart ollama
ollama pull deepseek-r1:70b
ollama list
ollama run deepseek-r1:70b

now installing a basic gui:
if no docker
  sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
  sudo apt install -y docker-ce
  sudo docker run hello-world

docker run -d -p 3000:8080 --add-host=host.docker.internal:172.31.7.208 -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main

docker logs -f open-webui

nohup ngrok http --url=racer-tolerant-solely.ngrok-free.app 3000 > ngrok.log 2>&1 &

nohup ngrok http --url=racer-tolerant-solely.ngrok-free.app 11434 > ngrok.log 2>&1 &  //just expose ollama service





## NOW WITH LLAMA 4

pip install llama-stack

llama model download --source meta --model-id Llama-4-Scout-17B-16E-Instruct

/root/.llama/checkpoints/Llama-4-Scout-17B-16E-Instruct

then, install llama.cpp (better create another env)

git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp

python3 convert_hf_to_gguf.py  \
  --outtype f16 \
  --outfile llama-4-Scout-17B-16E-Instruct.gguf \
  --tokenizer-path /root/.llama/checkpoints/Llama-4-Scout-17B-16E-Instruct/tokenizer.model \
  /root/.llama/checkpoints/Llama-4-Scout-17B-16E-Instruct/params.json

python3 convert_hf_to_gguf.py /root/.llama/checkpoints/Llama-4-Scout-17B-16E-Instruct  --outfile llama-4-Scout-17B-16E-Instruct.gguf
 
   





