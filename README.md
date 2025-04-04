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

docker run -d -p 3000:8080 --add-host=host.docker.internal:10.2.2.45 -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main

docker logs -f open-webui

nohup ngrok http --url=racer-tolerant-solely.ngrok-free.app 3000 > ngrok.log 2>&1 &



