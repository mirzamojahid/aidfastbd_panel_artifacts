import os
  from importlib.util import module_from_spec, spec_from_file_location
  _so = os.path.join(os.path.dirname(__file__), os.path.basename(__file__) + ".so")
  spec = spec_from_file_location(__name__, _so)
  mod = module_from_spec(spec)
  spec.loader.exec_module(mod)
  globals().update(mod.__dict__)
  