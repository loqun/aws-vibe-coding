import base64
from typing import Optional

class QRScanningService:
    @staticmethod
    def scan_qr_code(qr_data: str) -> Optional[str]:
        """Mock QR scanning - extract booking ID from QR data"""
        try:
            # Simple mock: assume QR data is base64 encoded booking ID
            decoded = base64.b64decode(qr_data).decode('utf-8')
            # Return the decoded booking ID (UUID format)
            return decoded if len(decoded) > 10 else None
        except:
            return None
    
    @staticmethod
    def generate_payment_qr(session_id: str, amount: float) -> str:
        """Generate QR code for additional payment"""
        payment_data = f"payment_{session_id}_{amount}"
        return base64.b64encode(payment_data.encode()).decode()

class PhotoCaptureService:
    @staticmethod
    def capture_parent_photo(image_data: str, staff_id: str) -> str:
        """Mock photo capture - return photo ID"""
        return f"photo_{staff_id}_{len(image_data)}"