import pytest
from main import is_pali

class TestClass:
    @pytest.mark.parametrize("word, expected", [
        ("Madam", True),
        ("Hello", False),
        ("Racecar", True),
        ("Python", False),
        ("Aibohphobia", True),
        ("", False)

    ])
    
    def test_is_pali(self, word, expected):
        assert is_pali(word) == expected
    
    def test_is_pali_raises_attribute_error(self):
        with pytest.raises(AttributeError):
            is_pali(123)
            is_pali(None)
            is_pali(["not", "a", "string"])
            is_pali(1.23)
            
        
if __name__ == "__main__":
    pytest.main()