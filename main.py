from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader
import os

os.environ['OPENAI_API_KEY'] = ''

#Loading from a directory
documents = SimpleDirectoryReader('your_directory').load_data()

text1 = 'خانواده سرفیس همیشه محصولاتی جذاب برای طرفداران تکنولوژی بوده‌اند. مایکروسافت با عرضه سرفیس لپ تاپ در سال تلاش کرد تا معیاری برای اولترابوک‌های پریمیوم ویندوزی به بازار عرضه کند اما پس از شش سال، هنوز این دستگاه نتوانسته به جایگاهی مناسب در این بازار متنوع دست پیدا کند. حالا نسل پنجم این لپ‌تاپ یعنی سرفیس لپ تاپ ۵ وارد بازار شده تا با مک بوک ایر ام ۲ و اولترابوک‌های زیبای بازار رقابت کند، اما آیا موفق می‌شود؟ در ادامه این مطلب با دیجیاتو همراه باشید.'
text2 = 'سرفیس لپ تاپ ۵ را فروشگاه یاسین رایان برای بررسی در اختیار دیجیاتو قرار داده است. یاسین رایان یکی از معتبرترین فروشگاه‌های اینترنتی است که بیش از ۹ سال به‌طور تخصصی محصولات مایکروسافت و خانواده سرفیس را به فروش می‌رساند. برای خرید انواع محصولات مایکروسافت می‌توانید به فروشگاه اینترنتی یاسین رایان مراجعه کنید.'

#Loading from strings, assuming you saved your data to strings text1, text2, ...
text_list = [text1, text2]
documents = [Document(t) for t in text_list]

#Construct a simple vector index
index = GPTSimpleVectorIndex(documents)

#Save your index to a index.json file
index.save_to_disk('index.json')
#Load the index from your saved index.json file
index = GPTSimpleVectorIndex.load_from_disk('index.json')
#Querying the index
response = index.query('یاسین رایان کیست؟')
print(response)
