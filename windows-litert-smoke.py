"""Synthetic raw [1,300,6] -> [1,6] mean model; no course data or trained weights."""
import platform,json
from importlib.metadata import version
import flatbuffers,numpy as np
from ai_edge_litert import schema_py_generated as s
from ai_edge_litert.interpreter import Interpreter,OpResolverType
model=s.ModelT();model.version=3
op_code=s.OperatorCodeT();op_code.builtinCode=s.BuiltinOperator.MEAN;op_code.deprecatedBuiltinCode=s.BuiltinOperator.MEAN;op_code.version=1;model.operatorCodes=[op_code]
b0=s.BufferT();b1=s.BufferT();b1.data=np.array([1],np.int32).view(np.uint8);model.buffers=[b0,b1]
g=s.SubGraphT();g.name='synthetic'
def tensor(name,shape,dtype,buffer):
 t=s.TensorT();t.name=name;t.shape=np.array(shape,np.int32);t.type=dtype;t.buffer=buffer;return t
inp=tensor('raw',[1,300,6],s.TensorType.FLOAT32,0);axis=tensor('axis',[1],s.TensorType.INT32,1);out=tensor('scores',[1,6],s.TensorType.FLOAT32,0)
g.tensors=[inp,axis,out];g.inputs=np.array([0],np.int32);g.outputs=np.array([2],np.int32)
op=s.OperatorT();op.opcodeIndex=0;op.inputs=np.array([0,1],np.int32);op.outputs=np.array([2],np.int32);op.builtinOptionsType=s.BuiltinOptions.ReducerOptions;op.builtinOptions=s.ReducerOptionsT();op.builtinOptions.keepDims=False;g.operators=[op];model.subgraphs=[g]
b=flatbuffers.Builder(1024);offset=model.Pack(b);b.Finish(offset,file_identifier=b'TFL3');data=bytes(b.Output())
it=Interpreter(model_content=data,experimental_op_resolver_type=OpResolverType.BUILTIN_WITHOUT_DEFAULT_DELEGATES);it.allocate_tensors()
x=np.random.default_rng(0).normal(size=(1,300,6)).astype(np.float32);it.set_tensor(it.get_input_details()[0]['index'],x);it.invoke();y=it.get_tensor(it.get_output_details()[0]['index']);np.testing.assert_allclose(y,x.mean(1),atol=1e-6,rtol=1e-5)
print(json.dumps({'os':platform.platform(),'python':platform.python_version(),'architecture':platform.machine(),'litert':version('ai-edge-litert'),'input':it.get_input_details()[0]['shape'].tolist(),'output':y.shape,'result':'PASS'}))
