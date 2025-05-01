
from transformers import AutoTokenizer
output_dir = "/content/drive/MyDrive/DL4H-Project/mimic-iv-note-di-bhc/models/Llama-2-7b-hf/mimic-iv-note-di-bhc_Llama-2-7b-hf_4000_600_chars_100_valid/lora_rank_8_lora_alpha_8_lora_dropout_0.05_num_target_modules_2_learning_rate_2e-5/"
tokenizer = AutoTokenizer.from_pretrained(f"{output_dir}/best_val_loss", trust_remote_code=True)

from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM

# Load base model config (from PEFT adapter)
config = PeftConfig.from_pretrained(f"{output_dir}/best_val_loss")

# Load the base model first (Llama2-7b)
base_model = AutoModelForCausalLM.from_pretrained(
    config.base_model_name_or_path,
    trust_remote_code=True,
    device_map="auto",
)

# Attach the fine-tuned PEFT adapter weights
model = PeftModel.from_pretrained(base_model, f"{output_dir}/best_val_loss")
model.eval()
