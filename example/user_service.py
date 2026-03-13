from typing import Any, Dict


class UserNotFoundError(Exception):
    """Raised when a user cannot be found."""


def get_user_from_db(user_id: int) -> Dict[str, Any]:
    if user_id < 0:
        raise UserNotFoundError(f"user {user_id} not found")

    # In a real app this would query a DB; here we hard-code a single record.
    if user_id == 1:
        return {"user_id": "1", "name": "alice", "is_active": "yes"}

    if user_id > 1000:
        # Pretend these users exist but are deactivated, with mixed types
        return {"user_id": str(user_id), "name": "legacy-user", "is_active": "no"}

    # Any other ID is "not found", but we raise a custom error instead of HTTPException.
    raise UserNotFoundError(f"user {user_id} not found")

