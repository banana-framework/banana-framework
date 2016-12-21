from __future__ import absolute_import

import pytest

from banana.app.base import Application


def test_app_become_immutable():
    Application._initialize = lambda a: None
    app = Application()
    assert not(app._Application__stop_mutation)
    setattr(app, 'test_attr', 'Test Value')
    assert app.test_attr == 'Test Value'
    delattr(app, '_Application__stop_mutation')
    app._after_initialization()
    stop_mutation_flag = getattr(app, '_Application__stop_mutation')
    assert isinstance(stop_mutation_flag, bool)
    assert stop_mutation_flag
    with pytest.raises(ValueError) as exc:
        setattr(app, 'another_attr', 'Test Value')
    assert str(exc.value) == 'Cannot modify Application object'
    with pytest.raises(ValueError) as exc:
        setattr(app, 'test_attr', 'Another Value')
    assert str(exc.value) == 'Cannot modify Application object'
    with pytest.raises(ValueError) as exc:
        delattr(app, 'test_attr')
    assert str(exc.value) == 'Cannot modify Application object'
