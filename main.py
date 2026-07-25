from openai import OpenAI
import os

from analyzer import analyze_controller
from context_builder import build_context
from documentation import generate_documentation


client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)


controller = """
[ApiController]
[Route("api/employees")]
public class EmployeesController : ControllerBase
{
    [HttpPost]
    public async Task<IActionResult> Create(CreateEmployeeDto dto)
    {
        return Ok();
    }
}
"""


analysis = analyze_controller(
    client,
    controller
)


context = build_context(
    controller,
    analysis
)


documentation = generate_documentation(
    client,
    context
)



os.makedirs(
    "output",
    exist_ok=True
)


with open(
    "output/API_Documentation.md",
    "w",
    encoding="utf-8"
) as file:
    file.write(documentation)


print("\n\n✅ Documentation generated")