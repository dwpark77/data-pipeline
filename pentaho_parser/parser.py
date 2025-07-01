import xml.etree.ElementTree as ET
from typing import List, Dict


def parse_pentaho_xml(path: str) -> List[Dict[str, str]]:
    """Parse a Pentaho transformation XML file and return lineage edges.

    Parameters
    ----------
    path : str
        Path to the Pentaho transformation XML file.

    Returns
    -------
    List[Dict[str, str]]
        A list of lineage edges mapping ``source`` to ``target`` steps.
    """
    tree = ET.parse(path)
    root = tree.getroot()

    # Pentaho files typically have a root <transformation> element
    transformation = root.find("transformation")
    if transformation is None:
        transformation = root

    steps = {}
    for step in transformation.findall("step"):
        name = step.findtext("name")
        if name:
            steps[name] = {"name": name}

    edges = []
    for hop in transformation.findall("hop"):
        src = hop.findtext("from")
        dst = hop.findtext("to")
        if src and dst:
            edges.append({"source": src, "target": dst})

    return edges
