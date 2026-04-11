# README.md — line-by-line analysis

## Lines 1-8
- Documentation text: # Nasiko.

## Lines 9-16
- Documentation text: [![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/).

## Lines 17-24
- Documentation text: [ CLI Tool](#-cli-tool) .

## Lines 25-32
- Documentation list items or steps: Nasiko is a developer control plane that transforms how you build, deploy, and manage AI agents at scale. Built with modern microservices architecture, Nasiko provides everything needed to run production AI agent ecosystems..

## Lines 33-40
- Documentation list items or steps: - ** AgentCard System** - Structured capability definitions for intelligent routing.

## Lines 41-48
- Documentation list items or steps: **Production Infrastructure:**.

## Lines 49-56
- Documentation list items or steps: - ** One-Command Setup** - `docker compose up -d` to full platform.

## Lines 57-64
- Documentation list items or steps: - ** Request Tracing** - End-to-end visibility across microservices via Arize Phoenix.

## Lines 65-72
- Starts or ends a code block or example.

## Lines 73-80
- Documentation text:               .

## Lines 81-88
- Documentation text:       Kong API Gateway       .

## Lines 89-96
- Documentation text:   /app/  Web Interface     .

## Lines 97-104
- Documentation text:    Core Platform              Intelligence                  AI Agents      .

## Lines 105-112
- Documentation text:  Agent Registry             LangChain Engine          crewai-workflows   .

## Lines 113-120
- Documentation text:                                                 .

## Lines 121-128
- Documentation text:  Role-Based Auth            Search & Filter                     .

## Lines 129-136
- Documentation text:  Auto-Registration                                                .

## Lines 137-144
- Documentation text:      Infrastructure &        .

## Lines 145-152
- Documentation text: :27017          :6379           :6006           (PostgSQL       (K8s)    .

## Lines 153-160
- Starts or ends a code block or example.

## Lines 161-168
- Starts or ends a code block or example.

## Lines 169-176
- Starts or ends a code block or example.

## Lines 177-184
- Documentation text: | Provider | API Key Env Var | Base URL | Models |.

## Lines 185-192
- Documentation list items or steps: ### Key Components.

## Lines 193-200
- Documentation list items or steps: - **Web Interface** (4000) - Browser dashboard accessible via Kong Gateway (/app/).

## Lines 201-208
- Starts or ends a code block or example.

## Lines 209-216
- Documentation text: git clone https://github.com/Nasiko-Labs/nasiko.git.

## Lines 217-224
- Section heading or comment: Example: 5kfdxaT7WRoseTKqksUY4gR2idR4FuBBEIQk5Cpzlek=.

## Lines 225-232
- Documentation text: # 4. Install Python dependencies (for CLI).

## Lines 233-240
- Starts or ends a code block or example.

## Lines 241-248
- Starts or ends a code block or example.

## Lines 249-256
- Documentation list items or steps: ** Success!** Access Nasiko at http://localhost:9100/app/.

## Lines 257-264
- Documentation list items or steps: ### Quick Links.

## Lines 265-272
- Starts or ends a code block or example.

## Lines 273-280
- Documentation text: uv sync.

## Lines 281-288
- Starts or ends a code block or example.

## Lines 289-296
- Starts or ends a code block or example.

## Lines 297-304
- Starts or ends a code block or example.

## Lines 305-312
- Starts or ends a code block or example.

## Lines 313-320
- Starts or ends a code block or example.

## Lines 321-328
- Starts or ends a code block or example.

## Lines 329-336
- Documentation text:  AgentCard.json          # Required: Agent capabilities.

## Lines 337-344
- Starts or ends a code block or example.

## Lines 345-352
- Documentation text: "description": "AI agent for document analysis and extraction",.

## Lines 353-360
- Documentation text: "analyze this contract",.

## Lines 361-368
- Starts or ends a code block or example.

## Lines 369-376
- Starts or ends a code block or example.

## Lines 377-384
- Documentation text: options: dict = {}.

## Lines 385-392
- Starts or ends a code block or example.

## Lines 393-400
- Starts or ends a code block or example.

## Lines 401-408
- Starts or ends a code block or example.

## Lines 409-416
- Starts or ends a code block or example.

## Lines 417-424
- Documentation text: nasiko agent upload-directory . --name my-agent.

## Lines 425-432
- Starts or ends a code block or example.

## Lines 433-440
- Documentation list items or steps: 1. **Query Analysis** - LangChain analyzes user intent and requirements.

## Lines 441-448
- Starts or ends a code block or example.

## Lines 449-456
- Starts or ends a code block or example.

## Lines 457-464
- Documentation list items or steps: All agents automatically receive:.

## Lines 465-472
- Documentation list items or steps: - **Nasiko Web UI**: http://localhost:9100/app/ - Integrated observability dashboard via Kong Gateway.

## Lines 473-480
- Starts or ends a code block or example.

## Lines 481-488
- Starts or ends a code block or example.

## Lines 489-496
- Starts or ends a code block or example.

## Lines 497-504
- Documentation text: GITHUB_CLIENT_SECRET=<your-github-oauth-secret>.

## Lines 505-512
- Documentation text: JWT_SECRET=<your-jwt-signing-secret>.

## Lines 513-520
- Documentation text: SUPERUSER_EMAIL=admin@example.com.

## Lines 521-528
- Starts or ends a code block or example.

## Lines 529-536
- Documentation text: | Web Interface | 4000 | Browser dashboard (access via Kong Gateway at /app/) |.

## Lines 537-544
- Documentation text: | Kong Registry | 8080 | Service discovery and registration |.

## Lines 545-552
- Starts or ends a code block or example.

## Lines 553-560
- Starts or ends a code block or example.

## Lines 561-568
- Documentation list items or steps: This command automatically:.

## Lines 569-576
- Starts or ends a code block or example.

## Lines 577-584
- Starts or ends a code block or example.

## Lines 585-592
- Documentation list items or steps: ### Production Architecture.

## Lines 593-600
- Documentation list items or steps: ##  Sample Agents.

## Lines 601-608
- Starts or ends a code block or example.

## Lines 609-616
- Starts or ends a code block or example.

## Lines 617-624
- Starts or ends a code block or example.

## Lines 625-632
- Documentation text: # View logs.

## Lines 633-640
- Starts or ends a code block or example.

## Lines 641-648
- Starts or ends a code block or example.

## Lines 649-656
- Starts or ends a code block or example.

## Lines 657-664
- Starts or ends a code block or example.

## Lines 665-672
- Documentation list items or steps: - `app-network` - Core services communication.

## Lines 673-680
- Documentation list items or steps: **Kong Gateway Routes** (http://localhost:9100):.

## Lines 681-688
- Documentation list items or steps: - **`/`** - Landing page (redirects to /app/).

## Lines 689-696
- Starts or ends a code block or example.

## Lines 697-704
- Documentation text: # Restart the listener if needed.

## Lines 705-712
- Starts or ends a code block or example.

## Lines 713-720
- Starts or ends a code block or example.

## Lines 721-728
- Starts or ends a code block or example.

## Lines 729-736
- Starts or ends a code block or example.

## Lines 737-744
- Documentation list items or steps: 5. Commit changes: `git commit -m 'Add amazing feature'`.

## Lines 745-752
- Documentation list items or steps: ##  Support.

## Lines 753-755
- Documentation text: <div align="center">.
