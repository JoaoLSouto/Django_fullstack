from http import HTTPStatus
from django.urls import reverse
import pytest
from django.contrib.auth.models import Permission


def test_contacts_thanks(client):
    # Given
    name = "Jhon"

    # Then
    response = client.get(reverse("contacts:thanks", args=(name,)))

    # Whhen
    assert response.status_code == HTTPStatus.OK
    assert response.content.decode() == f"Obrigado {name}!"


def test_contact_create_with_unauthenticated_user(client):
    # Given
    url = f'{reverse("accounts:login")}?next={reverse("contacts:create")}'
    # Then
    response = client.get("/contacts/create/")

    # When
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == url


@pytest.mark.django_db
def test_contact_create_success(client, django_user_model):
    # Given
    data = {
        "subject": "subject@testmail.com",
        "message": "Hello world!",
        "sender": "sender@testemail.com",
        "cc_myself": True,
    }
    user = django_user_model.objects.create_user(
        username="john", email="john@testmail.com", password="123mudar"
    )
    permission = Permission.objects.get(codename="add_contact")
    user.user_permissions.add(permission)
    # Then
    client.force_login(user)
    response = client.post(reverse("contacts:create"), data)

    # When
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse("contacts:thanks", args=(data["subject"],))
