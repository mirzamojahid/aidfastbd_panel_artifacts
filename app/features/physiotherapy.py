import importlib.util as _iu, os as _os, glob as _glob
_name = __name__.split('.')[-1]
_dir  = _os.path.dirname(__file__)
_candidates = (
    _glob.glob(_os.path.join(_dir, f"{_name}.cpython-*.so")) +
    _glob.glob(_os.path.join(_dir, f"{_name}.py.so")) +
    _glob.glob(_os.path.join(_dir, f"{_name}.so"))
)
if not _candidates:
    raise ImportError(f"Compiled module for {_name} not found in {_dir}")
_so = _candidates[0]
_spec = _iu.spec_from_file_location(__name__, _so)
_mod  = _iu.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
globals().update(_mod.__dict__)
