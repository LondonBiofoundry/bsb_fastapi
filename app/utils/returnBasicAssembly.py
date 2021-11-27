import basicsynbio as bsb
from app.utils.ItemtoPart import itemtopart


def return_build(mybuild) -> bsb.basicAssembly:
    try:
        assemblies = []
        for assembly in mybuild:
            parts = []
            for item in assembly.parts:
                part = itemtopart(item)
                parts.append(part)
            if assembly.name:
                parts.insert(0, assembly.name)
            else:
                parts.insert(0, assembly.id)
            mytuple = tuple(parts)
            assemblies.append(bsb.BasicAssembly(*mytuple))
        AssembliesTuple = tuple(assemblies)
        build = bsb.basicAssembly(*AssembliesTuple)
        return build
    except Exception as e:
        return {"error2": str(e)}
