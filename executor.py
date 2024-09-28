from concurrent.futures import ThreadPoolExecutor, as_completed

class Executor:
    def __init__(self):
        self.results = {}

    def run_pipeline(self, pipeline, modules):
        execution_order = pipeline.get_execution_order()  # Get topologically sorted order
        for module_name in execution_order:
            module = modules[module_name]
            # Gather inputs from dependencies
            dependencies_data = {dep: self.results[dep] for dep in pipeline.get_dependencies(module_name)}
            
            # Run the module and store the result
            result = module.run(dependencies_data)
            self.results[module_name] = result
            print(f"{module_name} completed with result: {result}")

class ParallelExecutor:
    def __init__(self):
        self.results = {}


    def run_pipeline(self,  pipeline, modules):
        ready_modules = pipeline.get_initial_modules()
        dependency_count = pipeline.get_dependency_count()

        with ThreadPoolExecutor() as executor:
            futures = {}

            for module_name in ready_modules:
                module = modules[module_name]
                future = executor.submit(self.run_module, module, {})
                futures[future] = module_name

            while futures:
                for future in as_completed(futures):
                    module_name = futures.pop(future)
                    try:
                        result = future.result()
                        self.results[module_name] = result
                        print(f"{module_name} completed with result: {result}")
                        
                        # Trigger dependent modules
                        dependents = pipeline.get_dependents(module_name)
                        for dep_module in dependents:
                            self.dependency_count[dep_module] -= 1
                            if self.dependency_count[dep_module] == 0:  # All dependencies resolved
                                dep_module_instance = modules[dep_module]
                                # Gather the outputs of all dependencies of this module
                                dependencies_data = {dep: self.results[dep] for dep in dep_module_instance.dependencies}
                                future = executor.submit(self.run, dep_module_instance, dependencies_data)
                                futures[future] = dep_module
                    except Exception as e:
                        print(f"Error in module {module_name}: {e}")
