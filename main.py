from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/submit_number', methods=['POST'])
def submit_number():
    number = request.form['number']
    # Логика обработки номера и создания данных для заполнения PDF
    data = {'name': 'John Doe', 'date': '2024-04-22'}

    fill_pdf_template('template.pdf', 'output.pdf', data)
    return 'PDF успешно создан!'

if __name__ == '__main__':
    app.run(debug=True)


def fill_pdf_template(template_path, output_path, data):
    with open(template_path, 'rb') as template_file:
        pdf_reader = PyPDF2.PdfReader(template_file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

            if '/Annots' in page:
                for annot in page['/Annots']:
                    if '/Subtype' in annot and annot['/Subtype'] == '/Widget':
                        field = annot['/T'][1:-1]
                        if field in data:
                            rect = annot['/Rect']
                            pdf_writer.update_page(page_num, {annot: {'/V': data[field]}})

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)
