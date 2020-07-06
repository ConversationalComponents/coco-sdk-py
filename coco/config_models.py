from typing import Dict, Optional, List

from pydantic import BaseModel


class TranslationConfig(BaseModel):
    # translate user inputs from source to target
    input_target_language: Optional[str]

    # translate component responses from source to target
    response_source_language: Optional[str]


class BlueprintConfig(BaseModel):
    blueprint_id: str
    translations: Optional[TranslationConfig]


class GlueNode(BaseModel):
    component_id: str
    on: Dict[str, str] = {}
    parameters: Dict[str, str] = {}
    position: Optional[Dict[str, int]]


class GlueConfig(BlueprintConfig):
    glue_v1: Dict[str, GlueNode]

class ActionsConfig(BlueprintConfig):
    action_config: Dict[str, List[str]]

class QaConfigNode(BaseModel):
    question_id: str
    questions: List[str]
    answers: List[str]

class QaConfig(BlueprintConfig):
    qa_config: List[QaConfigNode]