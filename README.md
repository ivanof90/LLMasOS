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

