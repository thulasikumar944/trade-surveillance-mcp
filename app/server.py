import os
from fastmcp import FastMCP

mcp = FastMCP("Trade Surveillance MCP")

TRADES = [
    {
        "trade_id": "T001",
        "symbol": "AAPL",
        "quantity": 5000,
        "risk": "HIGH"
    },
    {
        "trade_id": "T002",
        "symbol": "GOOGL",
        "quantity": 100,
        "risk": "LOW"
    },
    {
        "trade_id": "T003",
        "symbol": "MSFT",
        "quantity": 3000,
        "risk": "HIGH"
    }
]


@mcp.tool()
def get_trades(risk: str = "ALL") -> list:
    """Retrieve trades filtered by risk level."""

    if risk.upper() == "ALL":
        return TRADES

    return [
        trade for trade in TRADES
        if trade["risk"] == risk.upper()
    ]


@mcp.tool()
def get_alerts() -> list:
    """Retrieve active trade surveillance alerts."""

    return [
        {
            "alert_id": "A001",
            "trade_id": "T001",
            "severity": "HIGH",
            "reason": "Unusual trading volume"
        },
        {
            "alert_id": "A002",
            "trade_id": "T003",
            "severity": "MEDIUM",
            "reason": "Unusual price movement"
        }
    ]


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8080"))
    )