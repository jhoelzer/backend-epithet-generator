import pytest
from helpers import Vocabulary, EpithetGenerator

json_data = Vocabulary.read_json('resources/data.json')
one_epithet = EpithetGenerator().one_random()
multi_epithet = EpithetGenerator().multi_random(3)


def test_read_json_success():
    assert isinstance(json_data, dict)
    assert len(json_data.keys()) == 3
    assert 'Column 4' not in json_data.keys()
    assert 'odiferous' in json_data['Column 1']
    assert 'onion-eyed' in json_data['Column 2']
    assert 'maggot-pie' in json_data['Column 3']


def test_read_json_fail():
    with pytest.raises(AssertionError):
        assert isinstance(json_data, str)
    with pytest.raises(AssertionError):
        assert len(json_data.keys()) == 'Not a key'
    with pytest.raises(KeyError):
        assert json_data['Column 4']
    with pytest.raises(AssertionError):
        assert 'Not in Column 1' in json_data['Column 1']
    with pytest.raises(AssertionError):
        assert 'Not in Column 2' in json_data['Column 2']
    with pytest.raises(AssertionError):
        assert 'Not in Column 3' in json_data['Column 3']


def test_one_random_success():
    assert isinstance(one_epithet, str)
    assert len(one_epithet.split(' ')) == 3
    assert one_epithet.split(' ')[0] in json_data['Column 1']
    assert one_epithet.split(' ')[1] in json_data['Column 2']


def test_one_random_fail():
    with pytest.raises(AssertionError):
        assert isinstance(one_epithet, dict)
    with pytest.raises(AssertionError):
        assert len(one_epithet.split(' ')) == 333
    with pytest.raises(AssertionError):
        assert one_epithet.split(' ')[2] in json_data['Column 1']


def test_multi_random_success():
    assert isinstance(multi_epithet, list)
    assert len(multi_epithet) == 3
    assert multi_epithet[1].split(' ')[2].replace('') in json_data['Column 3']


def test_multi_random_fail():
    with pytest.raises(AssertionError):
        assert isinstance(multi_epithet, str)
    with pytest.raises(AssertionError):
        assert len(multi_epithet) == 101
    with pytest.raises(IndexError):
        assert multi_epithet[1].split(' ')[201]
