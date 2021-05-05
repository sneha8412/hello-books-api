
def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [""]
    
def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": "1",
        "title": "Ocean Book",
        "description": "watr 4evr"
    } 

def test_get_one_book_by_title(client, two_saved_books):
    # Act
    response = client.get("/books", query_string={"title": "Ocean Book"})
    response_body = response.get_json()


    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
        "title": "watr 4evr",
        "description" : "the red planet"
        }]
    
    
def test_create_one_planet(client):
    
    new_book_instance = Book(name="inner engineering", description="spirituality")
    response = client.post("/books", json=new_book_instance.to_json())
    response_body = response.get_data(as_text=True)

    assert response.status_code == 201
    assert response_body == '"inner engineering book successfully created"\n' 