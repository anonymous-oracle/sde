# test_minimax_provider.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for os/sys/pytest and mocks.

## Lines 9-16
- Imports patch/MagicMock and defines TestRouterConfigMiniMax class.

## Lines 17-24
- Tests default provider, patches env, and builds RouterConfig.

## Lines 25-32
- Asserts provider and starts minimax API key config test data.

## Lines 33-40
- Completes config data, instantiates RouterConfig, asserts fields.

## Lines 41-48
- Tests default MiniMax base URL from RouterConfig.

## Lines 49-56
- Tests custom MiniMax base URL override value.

## Lines 57-64
- Starts TestRoutingEngineLLMCreation class and docstring.

## Lines 65-72
- Sets provider/model/api/base for minimax config test.

## Lines 73-80
- Builds minimax config dict with model/temp/key/base_url.

## Lines 81-88
- Defines non-minimax config fallback branch.

## Lines 89-96
- Asserts minimax config fields and begins openai provider test.

## Lines 97-104
- Initializes openai provider config and minimax branch stub.

## Lines 105-112
- Adds openrouter branch config with base_url and keys.

## Lines 113-120
- Defines openai config fallback and asserts model/temperature.

## Lines 121-128
- Asserts no base_url and starts minimax temperature test.

## Lines 129-136
- Sets temperature based on provider and asserts > 0.

## Lines 137-144
- Tests minimax model fallback and starts openrouter base_url test.

## Lines 145-152
- Selects base_url per provider and asserts openrouter URL.

## Lines 153-160
- Starts TestMiniMaxModels class and default model test.

## Lines 161-168
- Defines valid model list and asserts highspeed availability.

## Lines 169-176
- Prepares model list for ordering test and asserts M2.7 before M2.5.

## Lines 177-184
- Defines legacy models list and checks M2.5 availability.

## Lines 185-192
- Continues legacy model assertions and starts framework detection class.

## Lines 193-200
- Defines LLM SDK mapping with minimax key.

## Lines 201-208
- Asserts minimax exists and maps to MiniMax display name.

## Lines 209-216
- Starts tracing instrumentation test class and mapping.

## Lines 217-224
- Asserts minimax uses OpenAI instrumentor mapping.

