from pydantic import BaseModel, Field, field_validator

class PasswordRequest(BaseModel):
    length: int = Field(12, ge=4, le=128, description="Длина пароля")
    use_digits: bool = Field(True, description="Включить цифры (0-9)")
    use_special: bool = Field(True, description="Включить спецсимволы (!@#$%^&*()_+-=[]{}|;:,.<>?)")
    use_uppercase: bool = Field(True, description="Включить заглавные буквы (A-Z)")

    @field_validator('length')
    @classmethod
    def validate_length(cls, v: int) -> int:
        if v < 4:
            raise ValueError('Длина пароля не может быть меньше 4 символов')
        if v > 128:
            raise ValueError('Длина пароля не может быть больше 128 символов')
        return v


class PasswordResponse(BaseModel):
    password: str = Field(..., description="Сгенерированный пароль")
    length: int = Field(..., description="Длина пароля")
    has_digits: bool = Field(..., description="Включены ли цифры")
    has_special: bool = Field(..., description="Включены ли спецсимволы")
    has_uppercase: bool = Field(..., description="Включены ли заглавные буквы")
