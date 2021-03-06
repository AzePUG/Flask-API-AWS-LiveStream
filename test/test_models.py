import pytest

from src.domain import model
from src.domain.exceptions import WrongFileExtensionModelException

def test_if_can_create_jpg():
    jpg = model.JPG(src_path="fake.jpg")
    assert jpg.extensions == (".jpeg", ".jpg")
    
def test_if_jpegs_are_equal():
    jpg1 = model.JPG(src_path="fake.jpg")
    jpg2 = model.JPG(src_path="fake.jpg")
    
    assert jpg1 == jpg2

def test_if_can_create_pdf():
    pdf = model.PDF(dest_path="fake.pdf")
    assert pdf.extension == ".pdf"
    
def test_if_pdfs_are_equal():
    pdf1 = model.PDF(dest_path="fake.pdf")
    pdf2 = model.PDF(dest_path="fake.pdf")
    
    assert pdf1 == pdf2
    
def test_if_can_allocate_jpeg():
    jpg = model.JPG(src_path="fake.jpg")
    assert model.allocate_jpeg(src_path="fake.jpg") == jpg

def test_if_can_allocate_pdf():
    pdf = model.PDF(dest_path="fake.pdf")
    assert model.allocate_pdf(dest_path="fake.pdf") == pdf
    
def test_if_cannot_allocate_pdf_with_wrong_extension():
    with pytest.raises(WrongFileExtensionModelException) as err:
        model.allocate_pdf(dest_path="fake.png")
    
    assert str(err.value) == "Wrong file extension: expected .pdf"
    
def test_if_cannot_allocate_jpeg():
    with pytest.raises(WrongFileExtensionModelException) as err:
        model.allocate_jpeg(src_path="fake.png")
    
    assert str(err.value) == "Wrong file extensions: expected .jpeg or .jpg"