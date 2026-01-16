clear

for model in \
  jamshid_mozafari/Meta-Llama-3-8B-Instruct-persianQA-finetuned-44415861-7915f60b \
  jamshid_mozafari/Meta-Llama-3-8B-Instruct-persianQA-f5fffacc-adbb5454 \

do
  for lang in english persian
  do
    python prompt.py --question_type factoid --prompt_type api --model "$model" --language "$lang" --finetune_inference True --api-key YOUR_TOGETHER_AI_API_KEY
  done
done

for model in \
  meta-llama/Meta-Llama-3-8B-Instruct-Lite \
  meta-llama/Llama-3.3-70B-Instruct-Turbo \
  Qwen/Qwen2.5-7B-Instruct-Turbo \
  Qwen/Qwen2.5-72B-Instruct-Turbo \
  mistralai/Mistral-Small-24B-Instruct-2501 \
  jamshid_mozafari/google/gemma-2-27b-it-4ba38cc8 \
  jamshid_mozafari/Dorna-Llama3-8B-Instruct-persianQA-afba6231-d1dbbaca \

do
  for lang in english persian
  do
    python prompt.py --question_type factoid --prompt_type api --model "$model" --language "$lang" --finetune_inference False --api-key YOUR_TOGETHER_AI_API_KEY
  done
done
