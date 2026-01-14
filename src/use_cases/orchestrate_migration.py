import os
import time

from src.adapters.observability import tracer
from src.domain.models import LegacyCode
from src.domain.reviewer_agent import ReviewerAgent


class MigrationOrchestrator:
    def __init__(self, ai_adapter, vector_db):
        self.ai_adapter = ai_adapter
        self.vector_db = vector_db

    async def handle_migration_event(self, data: dict):
        with tracer.start_as_current_span("ProcesandoMigracion"):
            print(f"👾 [LEVEL START] Analizando: {data['filename']}")
            start_time = time.time()

            # 1. Agente Arquitecto: Genera la propuesta
            legacy = LegacyCode(
                id="1",
                filename=data["filename"],
                content=data["content"],
                language=data["lang"],
            )
            plan = self.ai_adapter.generate_migration_plan(legacy)

            # 2. Agente Revisor: El "Kill Switch"
            # Pasamos el cliente de la IA para que el revisor haga su propia consulta
            reviewer = ReviewerAgent(self.ai_adapter.client)
            audit = reviewer.review_plan(str(plan))

            # Lógica de Failsafe (Kill Switch)
            if audit["audit_score"] < 5:
                print("🔨 THE HAMMER OF OPTIROMINIKILUS HAS FALLEN.")

                print(
                    f"🚨 [KILL SWITCH] Score de auditoría insuficiente ({audit['audit_score']}/10)."
                )
                print(
                    f"🗑️  Borrando propuesta fallida de {data['filename']} por seguridad..."
                )
                return

            # 3. Si pasa la auditoría, calculamos métricas de negocio
            processing_time = time.time() - start_time
            savings = (4 * 50) - 0.01
            output_path = f"output/report_{os.path.basename(data['filename'])}.md"

            # 4. Reporte Nintendocore con Sello de Seguridad
            header = f"# ⚔️ LANCER-AI REPORT: {data['filename']} ⚔️\n"
            ascii_art = "```text\n  LANCER - Nintendocore Edition\n```\n"
            body = (
                f"## 🕹️ Game Plan: {plan.suggested_architecture}\n"
                f"### 🛡️ Security Audit (SECOND BRAIN):\n"
                f"- **Status:** ✅ VALIDATED\n"
                f"- **Score:** {audit['audit_score']}/10\n"
                f"- **Observations:** {audit['observations']}\n\n"
                f"### 📝 Business Loot:\n"
                f"- **Gold Saved:** ${savings:.2f} USD\n"
                f"- **ROI:** {plan.estimated_roi_multiplier}x\n"
                f"- **Boss Defeated in:** {processing_time:.2f}s\n"
            )

            doc_content = header + ascii_art + body

            os.makedirs("output", exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(doc_content)

            print("🎸 [BREAKDOWN] ¡Migración validada y documentada!")
            print(f"📊 [BUSINESS_METRIC] Reporte generado en {output_path}")
