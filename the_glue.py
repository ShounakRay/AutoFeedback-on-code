from Modules.Code2Explanation.code2doc import Code2DocModule
from Modules.Code2Code.Extracontent.code_snippet_dataset import CodeSnippetDataset
from Modules.IntentClustering.data2clusters import IntentClustering

dataset = CodeSnippetDataset(languages=["Python"])
code_snippets = dataset.get_n_snippets(10)

code2doc = Code2DocModule(code_snippets)
data_with_docs = code2doc.get_docs()

doc2clusters = IntentClustering(data_with_docs['function_ids'], data_with_docs['code_reference'])
clusters = doc2clusters.get_clusters()

print(clusters)
