import CorrelationRate as CR
import text as txt
import Summarize as Sum

lda_path = "/Users/hongbowang/Personal/Spark Program/Spark Project/T1/output_K40/lda"
pip_path = "/Users/hongbowang/Personal/Spark Program/Spark Project/T1/output_K40/df_pip"
data_path = "/Users/hongbowang/Personal/Spark Program/Spark Project/T1/output_K40/result.json"
recomm_num = 1
line_num = 10

text = txt.sport

df, text = CR.recomm(text, data_path, pip_path, lda_path, recomm_num = recomm_num)

for i in range(len(text)):

    print("Suggest-", i+1, " : ", text[i], "\n")

    new_a = Sum.text_format(text[i])

    new_a[:] = [item for item in new_a if len(item) > 2]

    for idx, sentence in enumerate(Sum.summarizer(new_a, line_num, stopwords=Sum.stop_words)):

        print("%s. %s" % ((idx + 1), ' '.join(sentence)))

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")


# Pulling articles