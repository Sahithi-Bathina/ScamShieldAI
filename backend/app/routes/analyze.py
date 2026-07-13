from fastapi import APIRouter, HTTPException

from app.models.analyze_request import AnalyzeRequest
from app.agents.threat.agent import ThreatAgent

router = APIRouter(
    prefix="/analyze",
    tags=["Threat Analysis"]
)

threat_agent = ThreatAgent()


@router.post("/")
def analyze(request: AnalyzeRequest):
    try:
        result = threat_agent.analyze(request.text)
        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )