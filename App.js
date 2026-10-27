import React, { useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import {
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableOpacity,
  Image,
  Platform,
  Alert,
  KeyboardAvoidingView,
  ScrollView,
} from 'react-native';

export default function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    if (!email.trim() || !password.trim()) {
      Alert.alert(
        'Atenção',
        'Preencha o e-mail e a senha para continuar.'
      );
      return;
    }

    Alert.alert(
      'Login',
      'Campos preenchidos com sucesso! A autenticação ainda precisa ser configurada.'
    );

    // Não registre a senha no console.
    console.log('E-mail informado:', email.trim());
  };

  return (
    <KeyboardAvoidingView
      style={styles.keyboardContainer}
      behavior={Platform.OS === 'ios' ? 'padding' : undefined}
    >
      <ScrollView
        contentContainerStyle={styles.container}
        keyboardShouldPersistTaps="handled"
      >
        <View style={styles.loginCard}>
          <Text style={styles.title}>Login</Text>

          <Text style={styles.subtitle}>
            Almoxarifado SENAI
          </Text>

          <View style={styles.formGroup}>
            <Text style={styles.label}>E-mail</Text>

            <TextInput
              style={styles.input}
              placeholder="Digite seu e-mail"
              placeholderTextColor="#999"
              keyboardType="email-address"
              autoCapitalize="none"
              autoCorrect={false}
              autoComplete="email"
              value={email}
              onChangeText={setEmail}
              returnKeyType="next"
            />
          </View>

          <View style={styles.formGroup}>
            <Text style={styles.label}>Senha</Text>

            <TextInput
              style={styles.input}
              placeholder="Digite sua senha"
              placeholderTextColor="#999"
              secureTextEntry
              autoCapitalize="none"
              autoComplete="current-password"
              value={password}
              onChangeText={setPassword}
              onSubmitEditing={handleLogin}
              returnKeyType="done"
            />
          </View>

          <TouchableOpacity
            style={styles.btn}
            onPress={handleLogin}
            activeOpacity={0.8}
          >
            <Text style={styles.btnText}>Entrar</Text>
          </TouchableOpacity>
        </View>

        {/* Logo do SENAI: arquivo dentro da pasta static */}
        <Image
          source={require('./static/logosenai.jpg')}
          style={styles.logoSenai}
          resizeMode="contain"
          accessibilityLabel="Logo do SENAI"
        />

        <StatusBar style="dark" />
      </ScrollView>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  keyboardContainer: {
    flex: 1,
    backgroundColor: '#f2f2f2',
  },

  container: {
    flexGrow: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },

  loginCard: {
    width: '100%',
    maxWidth: 350,
    backgroundColor: '#ffffff',
    padding: 24,
    borderRadius: 8,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: Platform.OS === 'ios' ? 0.1 : 0.2,
    shadowRadius: 4,
    elevation: 3,
  },

  title: {
    textAlign: 'center',
    color: '#002D62',
    fontSize: 26,
    fontWeight: 'bold',
    marginBottom: 6,
  },

  subtitle: {
    textAlign: 'center',
    color: '#666',
    fontSize: 14,
    marginBottom: 24,
  },

  formGroup: {
    marginBottom: 16,
  },

  label: {
    marginBottom: 6,
    fontWeight: 'bold',
    color: '#333',
    fontSize: 14,
  },

  input: {
    width: '100%',
    paddingHorizontal: 12,
    paddingVertical: 12,
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 5,
    backgroundColor: '#fff',
    fontSize: 16,
    color: '#222',
  },

  btn: {
    width: '100%',
    paddingVertical: 14,
    backgroundColor: '#002D62',
    borderRadius: 5,
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 8,
  },

  btnText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },

  logoSenai: {
    width: 120,
    height: 55,
    marginTop: 24,
  },
});