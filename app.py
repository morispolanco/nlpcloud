import nlpcloud

client = nlpcloud.Client("gpt-j", "d57cc6ffb6230c3efdb8454068bbb5213655d4e8", gpu=True, lang="es")
client.gs_correction("Esto, estaa muy mal escrito")
