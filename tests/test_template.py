import postgrid
import os


def setup_module():
    postgrid.pm_key = os.environ.get("PM_API_KEY")


def create_test_template():
    return postgrid.Template.create(
        html="<b>test</b> template, hello {{to.firstName}}!",
        description="Test",
        metadata={"test": [10, 20]},
    )


def test_create():
    template = create_test_template()

    assert isinstance(template, postgrid.Template)
    assert isinstance(template.html, str)
    assert isinstance(template.description, str)
    assert template.html == "<b>test</b> template, hello {{to.firstName}}!"
    assert template.description == "Test"


def test_retrieve():
    template = create_test_template()
    assert isinstance(template, postgrid.Template)

    template = postgrid.Template.retrieve(template.id)
    assert isinstance(template, postgrid.Template)


def test_list():
    template = create_test_template()
    list_ = postgrid.Template.list()

    assert list_.total_count >= 1
    assert list_.skip == 0
    assert isinstance(list_.data[0], postgrid.Template)
    assert list_.data[0].html == template.html
    assert list_.data[0].description == template.description


def test_update():
    template = create_test_template()
    assert isinstance(template, postgrid.Template)

    template = postgrid.Template.update(
        template.id, html="updated template", description="updated description"
    )
    assert isinstance(template, postgrid.Template)
    assert template.html == "updated template"
    assert template.description == "updated description"


def test_delete():
    template = create_test_template()
    assert isinstance(template, postgrid.Template)

    res = postgrid.Template.delete(template.id)

    assert isinstance(res, postgrid.Template)
    assert res.deleted == True
