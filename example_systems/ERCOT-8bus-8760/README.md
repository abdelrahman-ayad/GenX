# ERCOT 8-bus system 

This examples shows the usage of DC_OPF related functions of GenX. 

To run the model, first navigate to the example directory:

- Using a Julia REPL:

```bash
$ julia
julia> cd("example_systems/ERCOT-8bus-8760/")
```

- Using a terminal or command prompt:
```bash
$ cd example_systems/ERCOT-8bus-8760/
``` 

Next, ensure that your settings in `settings/genx_settings.yml` are correct (the default settings use the solver `HiGHS`).

Once the settings are confirmed, run the model with the `Run.jl` script in the example directory:

- Using a Julia REPL (recommended)
```julia
julia> include("Run.jl")
```
- Using a terminal or command prompt:
```bash
$ julia Run.jl
```

Once the model has completed, results will write to the `results` directory.
