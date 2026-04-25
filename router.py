from fastapi import APIRouter, HTTPException, Query
from schemas import PasswordRequest, PasswordResponse
from service import generate_password

router = APIRouter(prefix="/password", tags=["password"])


@router.post("/generate", response_model=PasswordResponse)
def generate(data: PasswordRequest):
    password = generate_password(
        length=data.length,
        use_digits=data.use_digits,
        use_special=data.use_special,
        use_uppercase=data.use_uppercase
    )

    return PasswordResponse(
        password=password,
        length=data.length,
        has_digits=data.use_digits,
        has_special=data.use_special,
        has_uppercase=data.use_uppercase
    )

@router.get("/generate", response_model=PasswordResponse)
def generate_get(
        length: int = Query(12, ge=4, le=128, description="Длина пароля"),
        use_digits: bool = Query(True, description="Включить цифры"),
        use_special: bool = Query(True, description="Включить спецсимволы"),
        use_uppercase: bool = Query(True, description="Включить заглавные буквы")
    ):

        password = generate_password(length, use_digits, use_special, use_uppercase)

        return PasswordResponse(
            password=password,
            length=length,
            has_digits=use_digits,
            has_special=use_special,
            has_uppercase=use_uppercase
        )

@router.get("/check/{password}")
def check_password(password: str):
    if len(password) < 4:
        raise HTTPException(status_code=400, detail="Пароль слишком короткий (минимум 4 символа)")

    score = 0
    checks = {
        "length_ge_8": len(password) >= 8,
        "has_digits": any(c.isdigit() for c in password),
        "has_uppercase": any(c.isupper() for c in password),
        "has_special": any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    }
    score = sum(checks.values())

    strength_labels = ["Очень слабый", "Слабый", "Средний", "Хороший", "Отличный"]

    return {
        "password": password,
        "length": len(password),
        "score": score,
        "max_score": 4,
        "strength": strength_labels[score],
        "checks": checks
    }

