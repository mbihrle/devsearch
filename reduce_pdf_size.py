import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def compress_pdf(input_path, output_path):
    with open(input_path, 'rb') as input_file:
        reader = PdfFileReader(input_file)
        writer = PdfFileWriter()

        for i in range(reader.getNumPages()):
            writer.addPage(reader.getPage(i))

        writer.compressContentStreams()
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

# input_path = 'input.pdf'
# output_path = 'output.pdf'
# compress_pdf(input_path, output_path)

# import asposewordscloud
# from asposewordscloud.apis.words_api import WordsApi
# from asposewordscloud.models.requests import OptimizeDocumentRequest

# words_api = WordsApi()
# words_api.api_client.configuration.host = 'https://api.aspose.cloud'
# words_api.api_client.configuration.api_key['api_key'] = 'your_client_id'
# words_api.api_client.configuration.api_key['app_sid'] = 'your_client_secret'

# filename = 'input.pdf'
# remote_name = 'output.pdf'
# dest_folder = 'Temp'

# request = OptimizeDocumentRequest(filename=filename, folder=dest_folder, dest_file_name=remote_name)
# result = words_api.optimize_document(request)