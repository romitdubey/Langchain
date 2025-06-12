from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


llm = HuggingFacePipeline.from_model_id(
    model_id="sarvamai/sarvam-m",
    task="text-generation",
    pipeline_kwargs=dict({
        temprature: 0.5,
        max_new_tokens: 100}
    )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")
print(result.content)
