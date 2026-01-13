import pytest

@pytest.mark.asyncio
async def test_full_generation_cycle(manager_instance):
    """
    Requirement: The system must take a user story and return a success 
    status along with the path to the generated CSV test cases.
    """
    # Arrange
    raw_story = "As a user, I want to add items to my cart so I can purchase them later."
    
    # Act
    # Note: Ensure your manager.process_request is an async function
    result = await manager_instance.process_request(raw_story)
    
    # Assert
    assert result is not None, "The engine returned no response."
    assert result.get("status") == "success", f"Expected success, got {result.get('status')}"
    assert "csv_path" in result, "The response missing the generated artifact path."
    
    # Verify the file actually exists on disk
    assert os.path.exists(result["csv_path"]), "The generated CSV file was not found on disk."