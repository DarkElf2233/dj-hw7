
import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


# Test 1
# @pytest.mark.django_db
# def test_get_course(client, course_factory):
#     # Arrange
#     course = course_factory(_quantity=1)
#     # Act
#     response = client.get(f'/api/v1/courses/{course[0].id}')
#     # Assert
#     # assert response.status_code == 200
#     data = response.json()
#     print(data)
#     assert len(data) == len(course)
#     assert data['name'] == course[0].name


# Test 2
@pytest.mark.django_db
def test_get_courses(client, course_factory, student_factory):
    # Arrange
    students = student_factory(_quantity=3)
    courses = course_factory(students=students, _quantity=10)
    # Act
    response = client.get('/api/v1/courses/')
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


# Test 3
# @pytest.mark.django_db
# def test_get_courses_by_id(client, course_factory, student_factory):
#     # Arrange
#     students = student_factory(_quantity=3)
#     courses = course_factory(students=students, _quantity=10)
#     course_id = courses[0].id
#     # Act
#     response = client.get('/api/v1/courses/', id=course_id)
#     # Assert
#     assert response.status_code == 200
#     data = response.json()
#     assert data['id'] == course_id


# Test 4
# @pytest.mark.django_db
# def test_get_courses_by_name(client, course_factory, student_factory):
#     # Arrange
#     students = student_factory(_quantity=3)
#     courses = course_factory(students=students, _quantity=10)
#     course_name = courses[0].name
#     # Act
#     response = client.get('/api/v1/courses/', name=course_name)
#     # Assert
#     assert response.status_code == 200
#     data = response.json()
#     print(data)
#     for c in data:
#         assert course_name in c['name']


# Test 5
@pytest.mark.django_db
def test_post_course(client, student_factory):
    # Arrange
    count = Course.objects.count()
    students = student_factory(_quantity=3)
    # Act
    response = client.post('/api/v1/courses/', data={'name': 'Course', 'students': [u.id for u in students]})
    # Assert
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


# Test 6
# @pytest.mark.django_db
# def test_patch_course(client, course_factory, student_factory):
#     # Arrange
#     students = student_factory(_quantity=3)
#     course = course_factory(students=students, _quantity=1)
#     new_name = 'Course'
#     # Act
#     response = client.patch(f'/api/v1/courses/{course[0].id}', data={'name': new_name}, format='json')
#     # Assert
#     # assert response.status_code == 204
#     data = response.json()
#     assert data['name'] == new_name


# Test 7
@pytest.mark.django_db
def test_delete_course(client, course_factory, student_factory):
    # Arrange
    count = Course.objects.count()
    students = student_factory(_quantity=3)
    course = course_factory(students=students, _quantity=1)
    # Act
    response = client.delete(f'/api/v1/courses/{course[0].id}')
    # Assert
    assert response.status_code == 204
    assert Course.objects.count() == count - 1
