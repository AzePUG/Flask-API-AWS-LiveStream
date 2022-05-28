import pytest
import uuid

from src.domain import model
from src.domain.exceptions import WrongFileExtensionModelException

def test_if_can_create_jpg(get_uuid):
    jpg = model.JPG(code=get_uuid, src_path="fake.jpg")
    assert jpg.extensions == (".jpeg", ".jpg")
    
def test_if_jpegs_are_equal(get_uuid):
    jpg1 = model.JPG(code=get_uuid, src_path="fake.jpg")
    jpg2 = model.JPG(code=get_uuid, src_path="fake.jpg")
    
    assert jpg1 == jpg2

def test_if_can_create_pdf(get_uuid):
    pdf = model.PDF(code=get_uuid, dest_path="fake.pdf")
    assert pdf.extension == ".pdf"
    
def test_if_pdfs_are_equal(get_uuid):
    pdf1 = model.PDF(code=get_uuid, dest_path="fake.pdf")
    pdf2 = model.PDF(code=get_uuid, dest_path="fake.pdf")
    
    assert pdf1 == pdf2
    
def test_if_can_allocate_jpeg(get_uuid):
    jpg = model.JPG(code=get_uuid, src_path="fake.jpg")
    assert model.allocate_jpeg(code=get_uuid, src_path="fake.jpg") == jpg

def test_if_can_allocate_pdf(get_uuid):
    pdf = model.PDF(code=get_uuid, dest_path="fake.pdf")
    assert model.allocate_pdf(code=get_uuid, dest_path="fake.pdf") == pdf
    
def test_if_cannot_allocate_pdf_with_wrong_extension(get_uuid):
    with pytest.raises(WrongFileExtensionModelException) as err:
        model.allocate_pdf(code=get_uuid, dest_path="fake.png")
    
    assert str(err.value) == "Wrong file extension: expected .pdf"
    
def test_if_cannot_allocate_jpeg(get_uuid):
    with pytest.raises(WrongFileExtensionModelException) as err:
        model.allocate_jpeg(code=get_uuid, src_path="fake.png")
    
    assert str(err.value) == "Wrong file extensions: expected .jpeg or .jpg"
    
def test_jpg_model_from_dict(get_uuid, get_init_jpg_dict):
    pdf = model.JPG.from_dict(get_init_jpg_dict)
    assert pdf.code == get_uuid
    assert pdf.src_path == "fake.jpg"
    
def test_jpg_model_to_dict(get_uuid, get_init_jpg_dict):
    jpg = model.JPG.from_dict(get_init_jpg_dict)
    get_init_jpg_dict["extensions"] = jpg.extensions
    assert jpg.to_dict() == get_init_jpg_dict
    
    
def test_pdf_model_from_dict(get_uuid, get_init_pdf_dict):
    pdf = model.PDF.from_dict(get_init_pdf_dict)
    assert pdf.code == get_uuid
    assert pdf.dest_path == "fake.pdf"
    
def test_pdf_model_to_dict(get_uuid, get_init_pdf_dict):
    pdf = model.PDF.from_dict(get_init_pdf_dict)
    get_init_pdf_dict["extension"] = pdf.extension
    assert pdf.to_dict() == get_init_pdf_dict
    
def test_if_converted_model_is_created(get_uuid):
    jpg = model.JPG(code=get_uuid, src_path="fake.jpg")
    pdf = model.PDF(code=get_uuid, dest_path="fake.pdf")
    converted = model.Converted(converted_from=jpg, converted_to=pdf)
    assert converted.converted_to.code == get_uuid
    assert converted.converted_from.code == get_uuid